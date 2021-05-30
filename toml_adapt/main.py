import argparse
import sys
from toml_adapt.ManipulateToml import ManipulateToml

def start():
    parser = argparse.ArgumentParser(description='TOML manipulate')

    parser.add_argument('-path',
        type=str,
        help="Path to the .toml file")

    parser.add_argument('-a',
        choices=['change', 'add', 'remove'],
        help="Select action")

    parser.add_argument('-dep',
        type=str,
        help="Dependency name")

    parser.add_argument('-ver',
        type=str,
        help="Version of dependency")

    arguments = parser.parse_args()

    path = arguments.path
    action = arguments.a
    dependency = arguments.dep
    version = arguments.ver

    a = ManipulateToml(path, action, dependency, version)

    a.make_action()

    a.dump_to_file()
