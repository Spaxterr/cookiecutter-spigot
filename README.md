# Spigot Plugin Template
A [**Cookiecutter**](https://www.cookiecutter.io/) template for generating Spigot/Paper Minecraft plugin projects.

This template sets up a modern Java environment with industry-standard tooling for formatting, linting, and building Minecraft Spigot Plugins.

## Features
- **Build Systems:** Pre-configured **Maven** setup.
- **Configurable:** Versions and tooling are easily changed from their reasonable defaults.
- **Spotless** pre-configured and installed formatter with Google Java Style defaults.
- **PMD** pre-configured for naming conventions, security, and performance checks (`pmd-rules.xml`).

## Prerequisites
You need the following installed on your system:

1. **Java JDK 21** (or your target version).
2. **Maven**.
3. **Python** & **Cookiecutter**:
	```bash
	python3 -m pip install cookiecutter
	# or
	# uv pip install cookiecutter
	```

## Usage
Run the following command in your terminal to generate a new plugin:
```bash
cookiecutter 'https://github.com/Spaxterr/cookiecutter-spigot'
```

### Formatting (Spotless)
The project by default uses [**Spotless**](https://github.com/diffplug/spotless) (Google Java Format) for formatting. You will need to set your IDE up to use Spotless, or manually apply formatting with
```bash
mvn spotless:apply
```

### Linting (PMD)

The project by default uses [**PMD**](https://pmd.github.io/) for linting, pre-configured to check for common style issues, performance pitfalls, security risks and unused code. You will need to set your IDE up to use PMD for linting.

**IMPORTANT**: The PMD setup has to be configured to use the `pmd-rules.xml` file as its ruleset to use these guidelines.

PMD can also manually be executed with
```bash
pmd check --rulesets ./pmd-rules.xml --dir ./src
```
(given that PMD is installed as an executable)

---
## License
[MIT](https://www.google.com/url?sa=E&q=LICENSE)
