# GitHub Workflows Report

## Introduction

GitHub Actions is a powerful automation tool built into GitHub that allows you to automate tasks within your software development lifecycle. Workflows are custom automated processes that you can set up in your GitHub repository to build, test, package, release, or deploy any project.

## What is a Workflow?
A workflow is a configurable automated process made up of one or more jobs. Workflows are defined in YAML files stored in the `.github/workflows/` directory of your repository.


## Example Workflow 1: CI for a Python Project
Below is a simple example of a workflow file (`ci.yml`) that runs tests for a Python project:

```yaml
name: CI

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt
      - name: Run tests
        run: |
          pytest
```

## Example Workflow 2: Generate Python Code from Config
This workflow demonstrates how to generate a Python code file using configuration from a file stored in the `configs` folder. It uses a script (`generate_code.py`) that reads `configs/config.json` and generates `generated_code.py`.

```yaml
name: Generate Python Code from Config

on:
  workflow_dispatch:
  push:
    paths:
      - 'configs/**'
      - '.github/workflows/generate-code.yml'
      - 'generate_code.py'

jobs:
  generate:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Generate Python code from config
        run: |
          python generate_code.py
      - name: Show generated code
        run: |
          cat generated_code.py
```

### Sample Python Script: `generate_code.py`
This script reads a JSON config and generates a Python file:

```python
import json

# Path to the config file
config_path = 'configs/config.json'
# Path to the generated Python file
output_path = 'generated_code.py'

def main():
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    # Example: generate a Python file with a function using config values
    with open(output_path, 'w') as f:
        f.write('# This file is generated from config.json\n')
        f.write('def generated_function():\n')
        for key, value in config.items():
            f.write(f'    print("{key}: {value}")\n')

if __name__ == '__main__':
    main()
```


## Explanation of the Workflows

### CI Workflow
- **name:** The name of the workflow as it appears in GitHub Actions.
- **on:** Specifies the events that trigger the workflow (push or pull request to `main`).
- **jobs:** Defines a job named `build` that runs on the latest Ubuntu runner.
- **steps:**
  - Checks out the code.
  - Sets up Python 3.11.
  - Installs dependencies from `requirements.txt`.
  - Runs tests using `pytest`.

### Generate Python Code from Config Workflow
- **on:** Triggers on manual dispatch or when files in `configs/`, the workflow file, or `generate_code.py` change.
- **jobs:**
  - Checks out the code.
  - Sets up Python 3.11.
  - Runs the script to generate a Python file from the config.
  - Shows the generated code in the workflow logs.

## How to Use Workflows in a New Repository
1. Create a new repository on GitHub.
2. In your local project, create a directory: `.github/workflows/`.
3. Add a workflow YAML file (like the example above) to this directory.
4. Push your code to GitHub. The workflow will run automatically on the specified events.

## More Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)

## Conclusion
GitHub Actions workflows are a flexible way to automate your development process. You can customize workflows for building, testing, deploying, and more, tailored to your project's needs.
