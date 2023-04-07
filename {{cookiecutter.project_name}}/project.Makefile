## Add your own custom Makefile targets here

RUN = poetry run

.PHONY: check-jsonschema-example run-linkml-validation

check-jsonschema-example:
	# showing ignore failures here
	# this should be templated
	- $(RUN) check-jsonschema \
	  --schemafile project/jsonschema/my_awesome_schema.schema.json \
	  src/data/examples/invalid/PersonCollection-undefined-slot.yaml

run-linkml-validation:
	# PersonCollection is assumed as the target-class because it has been defined as the tree_root in the schema
	- $(RUN) linkml-validate \
	  --schema src/my_awesome_schema/schema/my_awesome_schema.yaml \
	  src/data/examples/invalid/PersonCollection-undefined-slot.yaml

