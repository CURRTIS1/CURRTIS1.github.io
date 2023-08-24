# Setting up Github Pages

## Pre-requisites

### Install mkdocs

Follow the below link to install `MKDocs`

["Getting Started with MKDocs@](https://www.mkdocs.org/getting-started/)

If you get the error `ModuleNotFoundError: No module named 'apt_pkg'` run the below:

```bash
sudo apt remove python3-apt
sudo apt autoremove
sudo apt autoclean
sudo apt install python3-apt
```

### Install Make

Run the below in your terminal

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install -y make
```

#### Make lint permissions

If you get permissions denied on the linting bash script, run the below:

```bash
sudo chmod a+x markdown-lint.sh
```

### Install Poetry

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

#### Error: /bin/bash: line 1: poetry: command not found

If you get the above error, ensure you have the correct path in your bash profile.

Run:

```bash
sudo nano ~/.bash_profile
```

Add the below:

```bash
export PATH="/home/curtis/.local/bin:$PATH"
```

## Set up Github actions

Run through the ["Quickstart for GitHub Pages"](https://docs.github.com/en/pages/quickstart).

Ensure you have created a branch called `gh-pages`

Go to your repo, actions and new workflow and add the following YAML template:

["Github Actions Workflow"](https://github.com/CURRTIS1/CURRTIS1.github.io/blob/main/.github/workflows/main.yml)
