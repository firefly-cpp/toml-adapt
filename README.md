<h1 align="center">
  toml-adapt
</h1>

<h2 align="center">
  A simple command-line interface (CLI) for manipulating toml files
</h2>

<p align="center">
  <a href="https://pypi.python.org/pypi">
    <img alt="PyPI Version" src="https://img.shields.io/pypi/v/toml-adapt.svg">
  </a>
  <img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/toml-adapt.svg">
  <img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/toml-adapt.svg">
  <a href="https://repology.org/project/toml-adapt/versions">
    <img alt="Packaging status" src="https://repology.org/badge/tiny-repos/toml-adapt.svg">
  </a>
  <a href="https://src.fedoraproject.org/rpms/python-toml-adapt">
    <img alt="Fedora package" src="https://img.shields.io/fedora/v/python3-toml-adapt?color=blue&label=Fedora%20Linux&logo=fedora">
  </a>
  <a href="https://aur.archlinux.org/packages/toml-adapt">
    <img alt="AUR package" src="https://img.shields.io/aur/version/toml-adapt?color=blue&label=Arch%20Linux&logo=arch-linux">
  </a>
  <a href="https://pepy.tech/project/toml-adapt">
    <img alt="Downloads" src="https://pepy.tech/badge/toml-adapt">
  </a>
  <a href="https://github.com/firefly-cpp/toml-adapt/blob/master/LICENSE">
    <img alt="GitHub license" src="https://img.shields.io/github/license/firefly-cpp/toml-adapt.svg">
  </a>
  <a href="https://github.com/firefly-cpp/toml-adapt/actions/workflows/python-app.yml">
    <img alt="GitHub Actions" src="https://github.com/firefly-cpp/toml-adapt/actions/workflows/python-app.yml/badge.svg">
  </a>
  <a href="https://toml-adapt.readthedocs.io/en/latest/?badge=latest">
    <img alt="Documentation Status" src="https://readthedocs.org/projects/toml-adapt/badge/?version=latest">
  </a>
</p>

<p align="center">
  <img alt="GitHub commit activity" src="https://img.shields.io/github/commit-activity/w/firefly-cpp/toml-adapt.svg">
  <a href='http://isitmaintained.com/project/firefly-cpp/toml-adapt "Average time to resolve an issue"'>
    <img alt="Average time to resolve an issue" src="http://isitmaintained.com/badge/resolution/firefly-cpp/toml-adapt.svg">
  </a>
  <a href='http://isitmaintained.com/project/firefly-cpp/toml-adapt "Percentage of issues still open"'>
    <img alt="Percentage of issues still open" src="http://isitmaintained.com/badge/open/firefly-cpp/toml-adapt.svg">
  </a>
  <a href="#-contributors">
    <img alt="All Contributors" src="https://img.shields.io/badge/all_contributors-4-orange.svg">
  </a>
</p>

<p align="center">
  <a href="https://doi.org/10.5281/zenodo.10467167">
    <img alt="DOI" src="https://zenodo.org/badge/DOI/10.5281/zenodo.10467167.svg">
  </a>
</p>

<p align="center">
  <a href="#-features">🚀 Features</a> •
  <a href="#️-supported-packaging-tools">🛠️ Supported packaging tools</a> •
  <a href="#-installation">📦 Installation</a> •
  <a href="#-usage">🚀 Usage</a> •
  <a href="#-cite-us">📄 Cite us</a> •
  <a href="#-license">🔑 License</a> •
  <a href="#-contributors">✨ Contributors</a>
</p>

Working with TOML files is becoming inevitable during the package maintenance process in different ecosystems. 🌐 Many times package maintainers must either change the version of dependency or add/remove dependencies when building their packages, due to the inconsistent base system. For example, solving this issue can be done either by using the provided patches or using sed commands. However, this may be slightly time-consuming and irritating. ⏳ A very simple yet user-friendly command line interface was developed in order to make this process easier. ⚙️📄🛠️

* **Free software:** MIT license
* **Python versions:** 3.8.x, 3.9.x, 3.10.x, 3.11.x, 3.12.x
* **Documentation:** https://toml-adapt.readthedocs.io/en/latest
* **Tested OS:** Windows, Ubuntu, Debian, Fedora, Alpine, Arch, macOS. **However, that does not mean it does not work on others.**

## 🚀 Features

CLI currently supports the following operations:

- adding/removing dependencies
- changing the  dependency version
- changing the dependency versions of all packages concurrently
- adding/removing/changing dev dependencies

## 🛠️ Supported packaging tools

The following packaging tools are currently supported by this software:

- poetry
- flit
- cargo
- julia (partly)

## 📦 Installation

### pip3

To install `toml-adapt` with pip, use:

```sh
pip install toml-adapt
```

### Fedora Linux

To install `toml-adapt` on Fedora, use:

```sh
$ dnf install python-toml-adapt
```

### Alpine Linux

To install `toml-adapt` on Alpine Linux, use:

```sh
$ apk add toml-adapt
```

### Arch Linux

To install `toml-adapt` on Arch Linux, use an [AUR helper](https://wiki.archlinux.org/title/AUR_helpers):

```sh
$ yay -Syyu toml-adapt
```

## 🚀 Usage

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

## 📄 Cite us

Fister, Jr., I., & Strajnar, F. (2024). firefly-cpp/toml-adapt: 0.3.1 (0.3.1). Zenodo. [https://doi.org/10.5281/zenodo.10467167](https://doi.org/10.5281/zenodo.10467167)

## 🔑 License

This package is distributed under the MIT License. This license can be found online at <http://www.opensource.org/licenses/MIT>.

## Disclaimer

This framework is provided as-is, and there are no guarantees that it fits your purposes or that it is bug-free. Use it at your own risk!

## ✨ Contributors

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="http://www.iztok-jr-fister.eu/"><img src="https://avatars.githubusercontent.com/u/1633361?v=4?s=100" width="100px;" alt="Iztok Fister Jr."/><br /><sub><b>Iztok Fister Jr.</b></sub></a><br /><a href="https://github.com/firefly-cpp/toml-adapt/commits?author=firefly-cpp" title="Code">💻</a> <a href="#platform-firefly-cpp" title="Packaging/porting to new platform">📦</a> <a href="#example-firefly-cpp" title="Examples">💡</a> <a href="#ideas-firefly-cpp" title="Ideas, Planning, & Feedback">🤔</a> <a href="#mentoring-firefly-cpp" title="Mentoring">🧑‍🏫</a> <a href="https://github.com/firefly-cpp/toml-adapt/commits?author=firefly-cpp" title="Documentation">📖</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/StrajnarFilip"><img src="https://avatars.githubusercontent.com/u/46705237?v=4?s=100" width="100px;" alt="StrajnarFilip"/><br /><sub><b>StrajnarFilip</b></sub></a><br /><a href="https://github.com/firefly-cpp/toml-adapt/commits?author=StrajnarFilip" title="Code">💻</a> <a href="https://github.com/firefly-cpp/toml-adapt/commits?author=StrajnarFilip" title="Tests">⚠️</a> <a href="#ideas-StrajnarFilip" title="Ideas, Planning, & Feedback">🤔</a> <a href="#example-StrajnarFilip" title="Examples">💡</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/musicinmybrain"><img src="https://avatars.githubusercontent.com/u/6898909?v=4?s=100" width="100px;" alt="Ben Beasley"/><br /><sub><b>Ben Beasley</b></sub></a><br /><a href="https://github.com/firefly-cpp/toml-adapt/commits?author=musicinmybrain" title="Documentation">📖</a> <a href="#platform-musicinmybrain" title="Packaging/porting to new platform">📦</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/kloczek"><img src="https://avatars.githubusercontent.com/u/31284574?v=4?s=100" width="100px;" alt="Tomasz Kłoczko"/><br /><sub><b>Tomasz Kłoczko</b></sub></a><br /><a href="https://github.com/firefly-cpp/toml-adapt/issues?q=author%3Akloczek" title="Bug reports">🐛</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://carlosal1015.github.io"><img src="https://avatars.githubusercontent.com/u/21283014?v=4?s=100" width="100px;" alt="Oromion"/><br /><sub><b>Oromion</b></sub></a><br /><a href="#platform-carlosal1015" title="Packaging/porting to new platform">📦</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/lahovniktadej"><img src="https://avatars.githubusercontent.com/u/57890734?v=4?s=100" width="100px;" alt="Tadej Lahovnik"/><br /><sub><b>Tadej Lahovnik</b></sub></a><br /><a href="https://github.com/firefly-cpp/toml-adapt/commits?author=lahovniktadej" title="Documentation">📖</a> <a href="#tutorial-lahovniktadej" title="Tutorials">✅</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
