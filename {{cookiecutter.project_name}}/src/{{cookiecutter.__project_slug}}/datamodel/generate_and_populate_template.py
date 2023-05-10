import csv
import click
import pandas as pd
from linkml.generators.excelgen import ExcelGenerator
from linkml_runtime import SchemaView
from schemasheets.schema_exporter import SchemaExporter


@click.command()
@click.option('--columns-to-insert', multiple=True, default=["slot", "class"],
              help='Columns to insert into the template')
@click.option('--columns-to-remove', multiple=True, default=["name", "annotations"],
              help='Columns to remove from the template')
@click.option('--destination-template', default='usage_template.tsv', help='Path to the destination template TSV file')
@click.option('--intermediate-excel-file', default="meta.xlsx",
              help='Where to store the Excel representation of the meta schema')
@click.option('--meta-path',
              default="https://raw.githubusercontent.com/linkml/linkml-model/main/linkml_model/model/schema/meta.yaml",
              help='URL or path to the schema meta file')
@click.option('--schema-path', type=click.Path(exists=True), required=True, help='Path to the schema file')
@click.option('--selected-sheet', default='slot_definition',
              help='Name of the selected sheet in the intermediate Excel file')
def generate_and_populate_template(schema_path: str, meta_path: str, selected_sheet: str, destination_template: str,
                                   columns_to_remove: list, columns_to_insert: list,
                                   intermediate_excel_file: str) -> None:
    """Generate a TSV representation of slot usages in a schema, guided by an XL representation of the metamodel.

    Args:
        schema_path (str): Path to the schema file.
        meta_path (str): URL or path to the schema meta file.
        selected_sheet (str): Name of the selected sheet in the intermediate Excel file.
        destination_template (str): Path to the destination template TSV file.
        columns_to_remove (list): Columns to remove from the template.
        columns_to_insert (list): Columns to insert into the template.
        intermediate_excel_file (str): Where to store the Excel representation of the meta schema.

    Returns:
        None
    """

    populated_file = destination_template.replace(".tsv", "_populated_raw.tsv")
    useful_file = destination_template.replace(".tsv", "_populated_no_blank_cols.tsv")

    meta_view = SchemaView(meta_path)
    excel_generator = ExcelGenerator(schema=meta_view.schema, output=intermediate_excel_file)
    excel_generator.serialize()

    df = pd.read_excel(intermediate_excel_file, sheet_name=selected_sheet)
    columns_for_template = list(df.columns)

    for column in columns_to_remove:
        if column in columns_for_template:
            columns_for_template.remove(column)

    columns_for_template.sort()

    for column in columns_to_insert:
        columns_for_template.insert(0, column)

    columns_for_template = [x.replace(" ", "_") for x in columns_for_template]
    second_header_row = columns_for_template.copy()
    second_header_row[0] = f">{second_header_row[0]}"
    sheet = [dict(zip(columns_for_template, second_header_row))]

    with open(destination_template, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=columns_for_template, delimiter='\t')
        writer.writeheader()
        writer.writerows(sheet)

    exporter = SchemaExporter()
    sv = SchemaView(schema_path)
    exporter.export(sv, specification=destination_template, to_file=populated_file)

    populated = pd.read_csv(populated_file, sep='\t')
    populated = populated.iloc[1:]
    populated = populated.dropna(axis=1, how='all')
    populated.to_csv(useful_file, sep='\t', index=False)


if __name__ == '__main__':
    generate_and_populate_template()
