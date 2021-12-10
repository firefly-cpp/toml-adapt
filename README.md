# toml-adapt --- Adapt toml files

---
[![PyPI Version](https://img.shields.io/pypi/v/toml-adapt.svg)](https://pypi.python.org/pypi/)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/toml-adapt.svg)
![PyPI - Downloads](https://img.shields.io/pypi/dm/toml-adapt.svg)
[![GitHub license](https://img.shields.io/github/license/firefly-cpp/toml-adapt.svg)](https://github.com/firefly-cpp/toml-adapt/blob/master/LICENSE)
![GitHub commit activity](https://img.shields.io/github/commit-activity/w/firefly-cpp/toml-adapt.svg)
[![Average time to resolve an issue](http://isitmaintained.com/badge/resolution/firefly-cpp/toml-adapt.svg)](http://isitmaintained.com/project/firefly-cpp/toml-adapt "Average time to resolve an issue")
[![Percentage of issues still open](http://isitmaintained.com/badge/open/firefly-cpp/toml-adapt.svg)](http://isitmaintained.com/project/firefly-cpp/toml-adapt "Percentage of issues still open")
![GitHub contributors](https://img.shields.io/github/contributors/firefly-cpp/toml-adapt.svg)
[![Fedora package](https://img.shields.io/fedora/v/python3-toml-adapt?color=blue&label=Fedora%20Linux&logo=fedora)](https://src.fedoraproject.org/rpms/python-toml-adapt)

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