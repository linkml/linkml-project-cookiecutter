import json
import click
import yaml


@click.command()
@click.option('--input-file', '-i', type=click.Path(exists=True), required=True,
              help='Path to the input JSON file')
@click.option('--output-file', '-o', type=click.Path(), required=True,
              help='Path to the output JSON file')
@click.option('--key', '-k', required=True, help='Name of the key to assign the list to')
@click.option('--output-format', '-f', type=click.Choice(['yaml', 'json'], case_sensitive=False),
              default="yaml", help='Output format')
def update_json(input_file, output_file, key, output_format):
    # Load the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Make sure the input is a list
    if not isinstance(data, list):
        raise click.BadParameter('Input JSON must contain a single list')

    # Create a new dictionary with the specified key and value
    updated_data = {key: data}

    if output_format == 'yaml':
        # Convert the dictionary to YAML
        with open(output_file, 'w') as f:
            yaml.dump(updated_data, f, sort_keys=False)
    elif output_format == 'json':
        # Save the updated object as a new JSON file
        with open(output_file, 'w') as f:
            json.dump(updated_data, f, indent=2)
    # could we ever get some other value?
    # should we warn?

    click.echo(f'Successfully updated JSON file with key "{key}"')


if __name__ == '__main__':
    update_json()
