toml-adapt
==========

Description
-----------

Working with TOML files is becoming inevitable during the package maintenance process in different ecosystems. Many times package maintainers must either change the version of dependency or add/remove dependencies when building their packages, due to the inconsistent base system. For example, solving this issue can be done either by using the provided patches or using sed commands. However, this may be slightly time-consuming and irritating. A very simple yet user-friendly command line interface was developed in order to make this process easier.

Features
~~~~~~~~

CLI currently supports the following operations:

- adding/removing dependencies
- changing the dependency version
- changing the dependency versions of all packages concurrently
- adding/removing/changing dev dependencies

Supported packaging tools
~~~~~~~~~~~~~~~~~~~~~~~~~

The following packaging tools are currently supported by this software:

- poetry
- flit
- cargo
- julia (partly)

Documentation
=============

The documentation is organized into the following sections:

* :ref:`user`
* :ref:`dev`
* :ref:`about`

.. _user:

.. toctree::
    :maxdepth: 2
    :caption: User documentation

    user/getting_started

.. _dev:

.. toctree::
   :maxdepth: 1
   :caption: Developer documentation

   dev/installation
   dev/testing
   dev/documentation

.. _about:

.. toctree::
   :maxdepth: 1
   :caption: About

   about/license
   about/code_of_conduct