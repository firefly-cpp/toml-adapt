Installation
============

Development environment
-----------------------

Requirements
~~~~~~~~~~~~

- Python: https://www.python.org
- Poetry: https://python-poetry.org/docs

After installing Poetry and cloning the project from GitHub, execute the following command in the root directory of the cloned project:

.. code:: sh

    $ poetry install

All of the project's dependencies should be installed and the project should be ready for further development. Note that Poetry creates a separate virtual environment for the project.

Development dependencies
~~~~~~~~~~~~~~~~~~~~~~~~

List of toml-adapt's dependencies:

+----------------------+----------------------+
| Package              | Version              |
+======================+======================+
| toml                 | *                    |
+----------------------+----------------------+
| click                | *                    |
+----------------------+----------------------+
| sphinx               | ^4.4.0               |
+----------------------+----------------------+
| sphinx-rtd-theme     | ^1.0.0               |
+----------------------+----------------------+

List of toml-adapt's development dependencies:

+----------------+--------------+
| Package        | Version      |
+================+==============+
| pytest         | ^6.2.5       |
+----------------+--------------+