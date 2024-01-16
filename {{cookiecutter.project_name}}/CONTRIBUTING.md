# Contributing to {{cookiecutter.project_name}}

:+1: First of all: Thank you for taking the time to contribute!

The following is a set of guidelines for contributing to
{{ cookiecutter.project_name }}. These guidelines are not strict rules.
Use your best judgment, and feel free to propose changes to this document
in a pull request.

## Table Of Contents

* [Code of Conduct](#code-of-conduct)
* [Guidelines for Contributions and Requests](#contributions)
  * [Reporting issues and making requests](#reporting-issues)
  * [Questions and Discussion](#questions-and-discussion)
  * [Adding new elements yourself](#adding-elements)
* [Best Practices](#best-practices)
  * [How to write a great issue](#great-issues)
  * [How to create a great pull/merge request](#great-pulls)

<a id="code-of-conduct"></a>

## Code of Conduct

The {{cookiecutter.project_name}} team strives to create a
welcoming environment for editors, users and other contributors.
Please carefully read our [Code of Conduct](CODE_OF_CONDUCT.md).

<a id="contributions"></a>

## Guidelines for Contributions and Requests

<a id="reporting-issues"></a>

### Reporting problems and suggesting changes to with the data model

Please use our [Issue Tracker][issues] for any of the following:

- Reporting problems
- Requesting new schema elements

<a id="questions-and-discussions"></a>

### Questions and Discussions

Please use our [Discussions forum][discussions] to ask general questions or contribute to discussions.

<a id="adding-elements"></a>

### Adding new elements yourself

Please submit a [Pull Request][pulls] to submit a new term for consideration.

<a id="best-practices"></a>

## Best Practices

<a id="great-issues"></a>

### GitHub Best Practice

- Creating and curating issues
    - Read ["About Issues"][[about-issues]]
    - Issues should be focused and actionable
    - Complex issues should be broken down into simpler issues where possible
- Pull Requests
    - Read ["About Pull Requests"][about-pulls]
    - Read [GitHub Pull Requests: 10 Tips to Know](https://blog.mergify.com/github-pull-requests-10-tips-to-know/)
    - Pull Requests (PRs) should be atomic and aim to close a single issue
    - Long running PRs should be avoided where possible
    - PRs should reference issues following standard conventions (e.g. “fixes #123”)
    - Schema developers should always be working on a single issue at any one time
    - Never work on the main branch, always work on an issue/feature branch
    - Core developers can work on branches off origin rather than forks
    - Always create a PR on a branch to maximize transparency of what you are doing
    - PRs should be reviewed and merged in a timely fashion by the {{cookiecutter.project_name}} technical leads
    - PRs that do not pass GitHub actions should never be merged
    - In the case of git conflicts, the contributor should try and resolve the conflict
    - If a PR fails a GitHub action check, the contributor should try and resolve the issue in a timely fashion

### Understanding LinkML

Core developers should read the material on the [LinkML site](https://linkml.io/linkml), in particular:

- [Overview](https://linkml.io/linkml/intro/overview.html)
- [Tutorial](https://linkml.io/linkml/intro/tutorial.html)
- [Schemas](https://linkml.io/linkml/schemas/index.html)
- [FAQ](https://linkml.io/linkml/faq/index.html)

### Modeling Best Practice

- Follow Naming conventions
    - Standard LinkML naming conventions should be followed (UpperCamelCase for classes and enums, snake_case for slots)
    - Know how to use the LinkML linter to check style and conventions
    - The names for classes should be nouns or noun-phrases: Person, GenomeAnnotation, Address, Sample
    - Spell out abbreviations and short forms, except where this goes against convention (e.g. do not spell out DNA)
    - Elements that are imported from outside (e.g. schema.org) need not follow the same naming conventions
    - Multivalued slots should be named as plurals
- Document model elements
    - All model elements should have documentation (descriptions) and other textual annotations (e.g. comments, notes)
    - Textual annotations on classes, slots and enumerations should be written with minimal jargon, clear grammar and no misspellings
- Include examples and counter-examples (intentionally invalid examples)
    - Rationale: these serve as documentation and unit tests
    - These will be used by the automated test suite
    - All elements of the nmdc-schema must be illustrated with valid and invalid data examples in src/data. New schema elements will not be merged into the main branch until examples are provided
    - Invalid example data files should be invalid for one single reason, which should be reflected in the filename. It should be possible to render the invalid example files valid by addressing that single fault.
- Use enums for categorical values
    - Rationale: Open-ended string ranges encourage multiple values to represent the same entity, like “water”, “H2O” and “HOH”
    - Any slot whose values could be constrained to a finite set should use an Enum
    - Non-categorical values, e.g. descriptive fields like `name` or `description` fall outside of this.
- Reuse
    - Existing scheme elements should be reused where appropriate, rather than making duplicative elements
    - More specific classes can be created by refinining classes using inheritance (`is_a`)

[about-branches]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches
[about-issues]: https://docs.github.com/en/issues/tracking-your-work-with-issues/about-issues
[about-pulls]: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests
[issues]: https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.project_name }}/issues/
[pulls]: https://github.com/{{ cookiecutter.github_org }}/{{ cookiecutter.project_name }}/pulls/

We recommend also reading [GitHub Pull Requests: 10 Tips to Know](https://blog.mergify.com/github-pull-requests-10-tips-to-know/)
