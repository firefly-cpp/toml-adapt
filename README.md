# toml-adapt --- Adapt toml files

---

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