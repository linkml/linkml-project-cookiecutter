import json
import click


@click.command()
@click.option('--input-file', '-i', type=click.Path(exists=True), required=True,
              help='Path to the input JSON file')
@click.option('--output-file', '-o', type=click.Path(), required=True,
              help='Path to the output JSON file')
@click.option('--key', '-k', required=True, help='Name of the key to assign the list to')
def update_json(input_file, output_file, key):
    # Load the input JSON file
    with open(input_file, 'r') as f:
        data = json.load(f)

    # Make sure the input is a list
    if not isinstance(data, list):
        raise click.BadParameter('Input JSON must contain a single list')

    # Create a new dictionary with the specified key and value
    updated_data = {key: data}

    # Save the updated object as a new JSON file
    with open(output_file, 'w') as f:
        json.dump(updated_data, f, indent=2)

    click.echo(f'Successfully updated JSON file with key "{key}"')


if __name__ == '__main__':
    update_json()
