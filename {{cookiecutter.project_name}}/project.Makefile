## Add your own custom Makefile targets here

RUN = poetry run

.PHONY: check-jsonschema-example run-linkml-validation

# {{cookiecutter.__source_path}}

check-jsonschema-example: project/jsonschema/{{cookiecutter.project_name}}.schema.json \
	  {{cookiecutter.project_name}}/src/data/examples/invalid/{{cookiecutter.main_schema_class}}Collection-undefined-slot.yaml
	# showing ignore failures here
	# this should be templated
	- $(RUN) check-jsonschema \
	  --schemafile $^

run-linkml-validation: {{cookiecutter.__source_path}} \
{{cookiecutter.project_name}}/src/data/examples/invalid/{{cookiecutter.main_schema_class}}Collection-undefined-slot.yaml
	# PersonCollection is assumed as the target-class because it has been defined as the tree_root in the schema
	- $(RUN) linkml-validate \
	  --schema $^