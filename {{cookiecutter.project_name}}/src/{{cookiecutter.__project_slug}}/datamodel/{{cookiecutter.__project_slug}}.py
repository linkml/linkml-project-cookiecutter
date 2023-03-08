# Auto generated from {{cookiecutter.__project_slug}}.yaml by pythongen.py version: 0.9.0
# Generation date: 2022-09-06T10:01:50
# Schema: my_datamodel
#
# id: https://w3id.org/my_org/my_datamodel
# description: Enter a detailed description of your project here
# license: https://creativecommons.org/publicdomain/zero/1.0/

import dataclasses
import re
from jsonasobj2 import as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.metamodelcore import Bool, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
PATO = CurieNamespace('PATO',
                      'http://purl.obolibrary.org/obo/PATO_')
BIOLINK = CurieNamespace('biolink',
                         'https://w3id.org/biolink/')
FAMREL = CurieNamespace('famrel',
                        'http://example.org/famrel/')
LINKML = CurieNamespace('linkml',
                        'https://w3id.org/linkml/')
MY_DATAMODEL = CurieNamespace('my_datamodel',
                              'https://w3id.org/my_org/my_datamodel')
PROV = CurieNamespace('prov',
                      'http://www.w3.org/ns/prov#')
SCHEMA = CurieNamespace('schema',
                        'http://schema.org/')
DEFAULT_ = MY_DATAMODEL

# Types


# Class references
class NamedThingId(extended_str):
    pass


class PersonId(NamedThingId):
    pass


class OrganizationId(NamedThingId):
    pass


@dataclass
class Registry(YAMLRoot):
    """
    Top level data container
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MY_DATAMODEL.Registry
    class_class_curie: ClassVar[str] = "my_datamodel:Registry"
    class_name: ClassVar[str] = "Registry"
    class_model_uri: ClassVar[URIRef] = MY_DATAMODEL.Registry

    persons: Optional[Union[
        Dict[Union[str, PersonId], Union[dict, "Person"]],
        List[Union[dict, "Person"]]
    ]] = empty_dict()

    organizations: Optional[Union[
        Dict[Union[str, OrganizationId], Union[dict, "Organization"]],
        List[Union[dict, "Organization"]]
    ]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_list(
            slot_name="persons",
            slot_type=Person,
            key_name="id",
            keyed=True
        )

        self._normalize_inlined_as_list(
            slot_name="organizations",
            slot_type=Organization,
            key_name="id",
            keyed=True
        )

        super().__post_init__(**kwargs)


@dataclass
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable entity
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MY_DATAMODEL.NamedThing
    class_class_curie: ClassVar[str] = "my_datamodel:NamedThing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = MY_DATAMODEL.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    description: Optional[str] = None
    image: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.description is not None \
           and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.image is not None and not isinstance(self.image, str):
            self.image = str(self.image)

        super().__post_init__(**kwargs)


@dataclass
class Person(NamedThing):
    """
    A person (alive, dead, undead, or fictional).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Person
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = MY_DATAMODEL.Person

    id: Union[str, PersonId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[str] = None
    age_in_years: Optional[int] = None
    current_address: Optional[Union[dict, "Address"]] = None
    has_familial_relationships: Optional[Union[
        Union[dict, "FamilialRelationship"],
        List[Union[dict, "FamilialRelationship"]]
    ]] = empty_list()
    aliases: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.primary_email is not None \
           and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None \
           and not isinstance(self.birth_date, str):
            self.birth_date = str(self.birth_date)

        if self.age_in_years is not None \
           and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.current_address is not None \
           and not isinstance(self.current_address, Address):
            self.current_address = Address(**as_dict(self.current_address))

        if not isinstance(self.has_familial_relationships, list):
            self.has_familial_relationships = [self.has_familial_relationships] \
                if self.has_familial_relationships is not None \
                else []
        self.has_familial_relationships = [
            v if isinstance(v, FamilialRelationship)
            else FamilialRelationship(**as_dict(v))
            for v in self.has_familial_relationships]

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v)
                        for v in self.aliases]

        super().__post_init__(**kwargs)


@dataclass
class HasAliases(YAMLRoot):
    """
    A mixin applied to any class that can have aliases/alternateNames
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MY_DATAMODEL.HasAliases
    class_class_curie: ClassVar[str] = "my_datamodel:HasAliases"
    class_name: ClassVar[str] = "HasAliases"
    class_model_uri: ClassVar[URIRef] = MY_DATAMODEL.HasAliases

    aliases: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v)
                        for v in self.aliases]

        super().__post_init__(**kwargs)


@dataclass
class Organization(NamedThing):
    """
    An organization such as a company or university
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.Organization
    class_class_curie: ClassVar[str] = "schema:Organization"
    class_name: ClassVar[str] = "Organization"
    class_model_uri: ClassVar[URIRef] = MY_DATAMODEL.Organization

    id: Union[str, OrganizationId] = None
    mission_statement: Optional[str] = None
    founding_date: Optional[str] = None
    aliases: Optional[Union[str, List[str]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OrganizationId):
            self.id = OrganizationId(self.id)

        if self.mission_statement is not None \
           and not isinstance(self.mission_statement, str):
            self.mission_statement = str(self.mission_statement)

        if self.founding_date is not None \
           and not isinstance(self.founding_date, str):
            self.founding_date = str(self.founding_date)

        if not isinstance(self.aliases, list):
            self.aliases = [self.aliases] if self.aliases is not None else []
        self.aliases = [v if isinstance(v, str) else str(v)
                        for v in self.aliases]

        super().__post_init__(**kwargs)


@dataclass
class Address(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA.PostalAddress
    class_class_curie: ClassVar[str] = "schema:PostalAddress"
    class_name: ClassVar[str] = "Address"
    class_model_uri: ClassVar[URIRef] = MY_DATAMODEL.Address

    street: Optional[str] = None
    city: Optional[str] = None
    postal_code: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.street is not None and not isinstance(self.street, str):
            self.street = str(self.street)

        if self.city is not None and not isinstance(self.city, str):
            self.city = str(self.city)

        if self.postal_code is not None \
           and not isinstance(self.postal_code, str):
            self.postal_code = str(self.postal_code)

        super().__post_init__(**kwargs)


@dataclass
class Relationship(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MY_DATAMODEL.Relationship
    class_class_curie: ClassVar[str] = "my_datamodel:Relationship"
    class_name: ClassVar[str] = "Relationship"
    class_model_uri: ClassVar[URIRef] = MY_DATAMODEL.Relationship

    started_at_time: Optional[Union[str, XSDDate]] = None
    ended_at_time: Optional[Union[str, XSDDate]] = None
    related_to: Optional[str] = None
    type: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self.started_at_time is not None \
           and not isinstance(self.started_at_time, XSDDate):
            self.started_at_time = XSDDate(self.started_at_time)

        if self.ended_at_time is not None \
           and not isinstance(self.ended_at_time, XSDDate):
            self.ended_at_time = XSDDate(self.ended_at_time)

        if self.related_to is not None \
           and not isinstance(self.related_to, str):
            self.related_to = str(self.related_to)

        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        super().__post_init__(**kwargs)


@dataclass
class FamilialRelationship(Relationship):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = MY_DATAMODEL.FamilialRelationship
    class_class_curie: ClassVar[str] = "my_datamodel:FamilialRelationship"
    class_name: ClassVar[str] = "FamilialRelationship"
    class_model_uri: ClassVar[URIRef] = MY_DATAMODEL.FamilialRelationship

    type: Union[str, "FamilialRelationshipType"] = None
    related_to: Union[str, PersonId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.type):
            self.MissingRequiredField("type")
        if not isinstance(self.type, FamilialRelationshipType):
            self.type = FamilialRelationshipType(self.type)

        if self._is_empty(self.related_to):
            self.MissingRequiredField("related_to")
        if not isinstance(self.related_to, PersonId):
            self.related_to = PersonId(self.related_to)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(text="ALIVE",
                             description="the person is living",
                             meaning=PATO["0001421"])
    DEAD = PermissibleValue(text="DEAD",
                            description="the person is deceased",
                            meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(text="UNKNOWN",
                               description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )


class FamilialRelationshipType(EnumDefinitionImpl):

    SIBLING_OF = PermissibleValue(text="SIBLING_OF",
                                  meaning=FAMREL["01"])
    PARENT_OF = PermissibleValue(text="PARENT_OF",
                                 meaning=FAMREL["02"])
    CHILD_OF = PermissibleValue(text="CHILD_OF",
                                meaning=FAMREL["01"])

    _defn = EnumDefinition(
        name="FamilialRelationshipType",
    )


# Slots
class slots:
    pass


slots.id = Slot(
    uri=SCHEMA.identifier,
    name="id",
    curie=SCHEMA.curie('identifier'),
    model_uri=MY_DATAMODEL.id,
    domain=None,
    range=URIRef
)

slots.name = Slot(
    uri=SCHEMA.name,
    name="name",
    curie=SCHEMA.curie('name'),
    model_uri=MY_DATAMODEL.name,
    domain=None,
    range=Optional[str]
)

slots.description = Slot(
    uri=SCHEMA.description,
    name="description",
    curie=SCHEMA.curie('description'),
    model_uri=MY_DATAMODEL.description,
    domain=None,
    range=Optional[str]
)

slots.image = Slot(
    uri=SCHEMA.image,
    name="image",
    curie=SCHEMA.curie('image'),
    model_uri=MY_DATAMODEL.image,
    domain=None,
    range=Optional[str]
)

slots.primary_email = Slot(
    uri=SCHEMA.email,
    name="primary_email",
    curie=SCHEMA.curie('email'),
    model_uri=MY_DATAMODEL.primary_email,
    domain=None,
    range=Optional[str]
)

slots.birth_date = Slot(
    uri=SCHEMA.birthDate,
    name="birth_date",
    curie=SCHEMA.curie('birthDate'),
    model_uri=MY_DATAMODEL.birth_date,
    domain=None,
    range=Optional[str]
)

slots.employed_at = Slot(
    uri=MY_DATAMODEL.employed_at,
    name="employed_at",
    curie=MY_DATAMODEL.curie('employed_at'),
    model_uri=MY_DATAMODEL.employed_at,
    domain=None,
    range=Optional[Union[str, OrganizationId]]
)

slots.is_current = Slot(
    uri=MY_DATAMODEL.is_current,
    name="is_current",
    curie=MY_DATAMODEL.curie('is_current'),
    model_uri=MY_DATAMODEL.is_current,
    domain=None,
    range=Optional[Union[bool, Bool]]
)

slots.has_familial_relationships = Slot(
    uri=MY_DATAMODEL.has_familial_relationships,
    name="has_familial_relationships",
    curie=MY_DATAMODEL.curie('has_familial_relationships'),
    model_uri=MY_DATAMODEL.has_familial_relationships,
    domain=None,
    range=Optional[Union[
        Union[dict, FamilialRelationship],
        List[Union[dict, FamilialRelationship]]
    ]]
)

slots.current_address = Slot(
    uri=MY_DATAMODEL.current_address, name="current_address",
    curie=MY_DATAMODEL.curie('current_address'),
    model_uri=MY_DATAMODEL.current_address, domain=None,
    range=Optional[Union[dict, Address]]
)

slots.age_in_years = Slot(
    uri=MY_DATAMODEL.age_in_years, name="age_in_years",
    curie=MY_DATAMODEL.curie('age_in_years'),
    model_uri=MY_DATAMODEL.age_in_years, domain=None, range=Optional[int]
)

slots.related_to = Slot(
    uri=MY_DATAMODEL.related_to,
    name="related_to",
    curie=MY_DATAMODEL.curie('related_to'),
    model_uri=MY_DATAMODEL.related_to,
    domain=None,
    range=Optional[str]
)

slots.type = Slot(
    uri=MY_DATAMODEL.type,
    name="type",
    curie=MY_DATAMODEL.curie('type'),
    model_uri=MY_DATAMODEL.type,
    domain=None,
    range=Optional[str]
)

slots.street = Slot(
    uri=MY_DATAMODEL.street,
    name="street",
    curie=MY_DATAMODEL.curie('street'),
    model_uri=MY_DATAMODEL.street,
    domain=None,
    range=Optional[str]
)

slots.city = Slot(
    uri=MY_DATAMODEL.city,
    name="city",
    curie=MY_DATAMODEL.curie('city'),
    model_uri=MY_DATAMODEL.city,
    domain=None,
    range=Optional[str]
)

slots.mission_statement = Slot(
    uri=MY_DATAMODEL.mission_statement,
    name="mission_statement",
    curie=MY_DATAMODEL.curie('mission_statement'),
    model_uri=MY_DATAMODEL.mission_statement,
    domain=None,
    range=Optional[str]
)

slots.founding_date = Slot(
    uri=MY_DATAMODEL.founding_date,
    name="founding_date",
    curie=MY_DATAMODEL.curie('founding_date'),
    model_uri=MY_DATAMODEL.founding_date,
    domain=None,
    range=Optional[str]
)

slots.postal_code = Slot(
    uri=MY_DATAMODEL.postal_code,
    name="postal_code",
    curie=MY_DATAMODEL.curie('postal_code'),
    model_uri=MY_DATAMODEL.postal_code,
    domain=None,
    range=Optional[str]
)

slots.started_at_time = Slot(
    uri=PROV.startedAtTime,
    name="started_at_time",
    curie=PROV.curie('startedAtTime'),
    model_uri=MY_DATAMODEL.started_at_time,
    domain=None,
    range=Optional[Union[str, XSDDate]]
)

slots.ended_at_time = Slot(
    uri=PROV.endedAtTime,
    name="ended_at_time",
    curie=PROV.curie('endedAtTime'),
    model_uri=MY_DATAMODEL.ended_at_time,
    domain=None,
    range=Optional[Union[str, XSDDate]]
)

slots.registry__persons = Slot(
    uri=MY_DATAMODEL.persons,
    name="registry__persons",
    curie=MY_DATAMODEL.curie('persons'),
    model_uri=MY_DATAMODEL.registry__persons,
    domain=None,
    range=Optional[Union[
        Dict[Union[str, PersonId], Union[dict, Person]],
        List[Union[dict, Person]]
    ]]
)

slots.registry__organizations = Slot(
    uri=MY_DATAMODEL.organizations,
    name="registry__organizations",
    curie=MY_DATAMODEL.curie('organizations'),
    model_uri=MY_DATAMODEL.registry__organizations,
    domain=None,
    range=Optional[Union[
        Dict[Union[str, OrganizationId], Union[dict, Organization]],
        List[Union[dict, Organization]]
    ]]
)

slots.hasAliases__aliases = Slot(
    uri=MY_DATAMODEL.aliases,
    name="hasAliases__aliases",
    curie=MY_DATAMODEL.curie('aliases'),
    model_uri=MY_DATAMODEL.hasAliases__aliases,
    domain=None,
    range=Optional[Union[str, List[str]]]
)

slots.related_to = Slot(
    uri=MY_DATAMODEL.related_to,
    name="related to",
    curie=MY_DATAMODEL.curie('related_to'),
    model_uri=MY_DATAMODEL.related_to,
    domain=None,
    range=Union[str, PersonId]
)

slots.Person_primary_email = Slot(
    uri=SCHEMA.email,
    name="Person_primary_email",
    curie=SCHEMA.curie('email'),
    model_uri=MY_DATAMODEL.Person_primary_email,
    domain=Person,
    range=Optional[str],
    pattern=re.compile(r'^\S+@[\S+\.]+\S+')
)

slots.FamilialRelationship_type = Slot(
    uri=MY_DATAMODEL.type,
    name="FamilialRelationship_type",
    curie=MY_DATAMODEL.curie('type'),
    model_uri=MY_DATAMODEL.FamilialRelationship_type,
    domain=FamilialRelationship,
    range=Union[str, "FamilialRelationshipType"]
)

slots.FamilialRelationship_related_to = Slot(
    uri=MY_DATAMODEL.related_to,
    name="FamilialRelationship_related to",
    curie=MY_DATAMODEL.curie('related_to'),
    model_uri=MY_DATAMODEL.FamilialRelationship_related_to,
    domain=FamilialRelationship,
    range=Union[str, PersonId]
)
