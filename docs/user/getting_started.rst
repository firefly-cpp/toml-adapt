Getting started
===============

This section demonstrates the usage of the toml-adapt framework.

Installation
------------

To install the toml-adapt package, run the following command:

.. code:: bash

    pip install toml-adapt

Usage
-----

``-a`` Available actions are:

- add
- remove
- change
- add-dev
- remove-dev
- change-dev

``-path`` Specifies the path to the TOML file you wish to edit.

``-dep`` This option sets the name of dependency you wish to manipulate. Reserved keyword ``ALL`` will instead do action on all dependencies. 

``-ver`` This option sets the version. With Python Poetry, there is reserved keyword ``X``, which will become ``*`` (meaning it accepts any version of dependency).

The following are examples of usage:

Change dependency
~~~~~~~~~~~~~~~~~
.. code:: sh

    toml-adapt -path pyproject.toml -a change -dep niaclass -ver 0.1.0


Add dependency
~~~~~~~~~~~~~~

.. code:: sh

    toml-adapt -path pyproject.toml -a add -dep niaclass -ver 0.1.0


Remove dependency
~~~~~~~~~~~~~~~~~

.. code:: sh
    
    toml-adapt -path pyproject.toml -a remove -dep niaclass -ver 0.1.0


Other examples
~~~~~~~~~~~~~~

Change all existing dependencies in toml file

.. code:: sh

    toml-adapt -path pyproject.toml -a change -dep ALL -ver X

X represents a *

How to use it in SPEC files?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: sh

    %prep
    ...
        
    ## Make dependencies consistent with Fedora dependencies
        
    toml-adapt -path pyproject.toml -a change -dep ALL -ver X
