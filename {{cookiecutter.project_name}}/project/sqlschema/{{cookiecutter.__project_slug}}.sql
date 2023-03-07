CREATE TABLE "Address" (
    street TEXT,
    city TEXT,
    postal_code TEXT,
    PRIMARY KEY (street, city, postal_code)
);

CREATE TABLE "NamedThing" (
    id TEXT NOT NULL,
    name TEXT,
    description TEXT,
    image TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE "Organization" (
    id TEXT NOT NULL,
    name TEXT,
    description TEXT,
    image TEXT,
    mission_statement TEXT,
    founding_date TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE "Person" (
    id TEXT NOT NULL,
    name TEXT,
    description TEXT,
    image TEXT,
    primary_email TEXT,
    birth_date TEXT,
    age_in_years INTEGER,
    current_address TEXT,
    PRIMARY KEY (id)
);

CREATE TABLE "Registry" (
    persons TEXT,
    organizations TEXT,
    PRIMARY KEY (persons, organizations)
);

CREATE TABLE "Relationship" (
    started_at_time DATE,
    ended_at_time DATE,
    related_to TEXT,
    type TEXT,
    PRIMARY KEY (started_at_time, ended_at_time, related_to, type)
);

CREATE TABLE "FamilialRelationship" (
    started_at_time DATE,
    ended_at_time DATE,
    related_to TEXT NOT NULL,
    type VARCHAR(10) NOT NULL,
    "Person_id" TEXT,
    PRIMARY KEY (started_at_time, ended_at_time, related_to, type, "Person_id"),
    FOREIGN KEY(related_to) REFERENCES "Person" (id),
    FOREIGN KEY("Person_id") REFERENCES "Person" (id)
);

CREATE TABLE "Organization_aliases" (
    backref_id TEXT,
    aliases TEXT,
    PRIMARY KEY (backref_id, aliases),
    FOREIGN KEY(backref_id) REFERENCES "Organization" (id)
);

CREATE TABLE "Person_aliases" (
    backref_id TEXT,
    aliases TEXT,
    PRIMARY KEY (backref_id, aliases),
    FOREIGN KEY(backref_id) REFERENCES "Person" (id)
);
