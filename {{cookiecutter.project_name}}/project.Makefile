## Add your own custom Makefile targets here

RUN = poetry run

.PHONY: check-jsonschema-example

check-jsonschema-example:
	# showing ignore failures more
	# this should be templated
	- poetry run check-jsonschema \
	  --schemafile project/jsonschema/my_awesome_schema.schema.json \
	  src/data/examples/invalid/PersonCollection-undefined-slot.yaml