import json
import os
import click


@click.command()
@click.option('--input-file', '-i', type=click.Path(exists=True), required=True,
              help='Path to the input JSON file')
@click.option('--output-dir', '-o', type=click.Path(), required=True,
              help='Path to the output directory')
def extract_lists(input_file, output_dir):
    # Load the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Make sure the input is a dictionary with one or more key-value pairs,
    # where the values are lists
    if not isinstance(data, dict):
        raise click.BadParameter('Input JSON must contain a dictionary with one or more key-value pairs')

    for key, value in data.items():
        if not isinstance(value, list):
            raise click.BadParameter(f'Value for key "{key}" must be a list')

        # Save each list as a new JSON file with the same name as the key
        output_file = os.path.join(output_dir, f'{key}.json')
        with open(output_file, 'w') as f:
            json.dump(value, f)

        click.echo(f'Successfully extracted list from key "{key}" in "{input_file}" and saved it as "{output_file}"')


if __name__ == '__main__':
    extract_lists()
