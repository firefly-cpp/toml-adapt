# toml-adapt --- Adapt toml files

---

## Description
This is a very simple package for manipulating toml format files. This is still a work in progress. Recent version of this package supports the manipulation of dependencies that are included in toml files.

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
