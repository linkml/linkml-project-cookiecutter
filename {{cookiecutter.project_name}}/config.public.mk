# config.public.mk

# This file is public in git. No sensitive info allowed.
# These variables are sourced in Makefile, following make-file conventions.
# Be aware that this file does not follow python or bash conventions, so may appear a little unfamiliar.

###### schema definition variables, used by makefile

# Note: makefile variables should not be quoted, as makefile handles quoting differently than bash
LINKML_SCHEMA_NAME="{{cookiecutter.__project_slug}}"
LINKML_SCHEMA_AUTHOR="{{cookiecutter.__author}}"
LINKML_SCHEMA_DESCRIPTION="{{cookiecutter.project_description}}"
LINKML_SCHEMA_SOURCE_PATH="{{cookiecutter.__source_path}}"
LINKML_SCHEMA_GOOGLE_SHEET_MODULE="{{cookiecutter.__google_sheet_module}}"
LINKML_SCHEMA_GOOGLE_SHEET_ID="{{cookiecutter.google_sheet_id}}"
LINKML_SCHEMA_GOOGLE_SHEET_TABS="{{cookiecutter.google_sheet_tabs}}"
LINKML_USE_SCHEMASHEETS={{cookiecutter.use_schemasheets}}

###### linkml generator variables, used by makefile

## gen-project configuration file
LINKML_GENERATORS_CONFIG_YAML=config.yaml

## pass args if gendoc ignores config.yaml (i.e. --no-mergeimports)
LINKML_GENERATORS_DOC_ARGS=

## pass args to workaround genowl rdfs config bug (linkml#1453)
##   (i.e. --no-type-objects --no-metaclasses --metadata-profile rdfs)
LINKML_GENERATORS_OWL_ARGS=

## pass args to trigger experimental java/typescript generation
LINKML_GENERATORS_JAVA_ARGS=
LINKML_GENERATORS_TYPESCRIPT_ARGS=
