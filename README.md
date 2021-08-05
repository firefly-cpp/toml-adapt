# toml-adapt --- Adapt toml files

---

## Description
This is a very simple package for manipulating toml format files. This is still a work in progress. Recent version of this package supports the manipulation of dependencies that are included in toml files.

## Installation

### pip3

Install toml-adapt with pip3:

```sh
pip3 install toml-adapt
```

### Fedora Linux

To install toml-adapt on Fedora, use:

```sh
$ dnf install python-toml-adapt
```

## Usage

### Change dependency
```sh
toml-adapt -path pyproject.toml -a change -dep niaclass -ver 0.1.0
```

### Add dependency
```sh
toml-adapt -path pyproject.toml -a add -dep niaclass -ver 0.1.0
```

### Remove dependency
```sh
toml-adapt -path pyproject.toml -a remove -dep niaclass -ver 0.1.0
```

### Other examples

Change all existing dependencies in toml file
```sh
toml-adapt -path pyproject.toml -a change -dep ALL -ver X
```
X represents a *

### How to use it in SPEC files?

```sh
%prep
...
	
# Make dependencies consistent with Fedora dependencies
	
toml-adapt -path pyproject.toml -a change -dep ALL -ver X
```