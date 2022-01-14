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
Working with TOML files is becoming inevitable during the package maintenance process in different ecosystems. Many times package maintainers must either change the version of dependency or add/remove dependencies when building their packages, due to the inconsistent base system. For example, solving this issue can be done either by using the provided patches or using sed commands. However, this
may be slightly time-consuming and irritating. A very simple yet user-friendly command line interface was developed in order to make this process easier.

### Features

CLI currently supports the following operations:

- adding/removing dependencies
- changing the  dependency version
- changing the dependency versions of all packages concurrently
- adding/removing/changing dev dependencies

### Supported packaging tools

The following packaging tools are currently supported by this software:

- poetry
- flit
- cargo
- julia (partly)

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

### Usage

`-a` Available actions are:
- add
- remove
- change
- add-dev
- remove-dev
- change-dev

`-path` Specifies the path to the TOML file you wish to edit.

`-dep` This option sets the name of dependency you wish to manipulate. Reserved keyword `ALL` will instead do action on all dependencies. 

`-ver` This option sets the version. With Python Poetry, there is reserved keyword `X`, which will become `*` (meaning it accepts any version of dependency).

The following are examples of usage:

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
	
## Make dependencies consistent with Fedora dependencies
	
toml-adapt -path pyproject.toml -a change -dep ALL -ver X
```

## License

This package is distributed under the MIT License. This license can be found online at <http://www.opensource.org/licenses/MIT>.

## Disclaimer

This framework is provided as-is, and there are no guarantees that it fits your purposes or that it is bug-free. Use it at your own risk!
