import argparse
import sys
from toml_adapt.ManipulateToml import ManipulateToml

def start():
    parser = argparse.ArgumentParser(description='TOML manipulate')

    parser.add_argument('-path',
        type=str,
        help="Path to the .toml file")

    parser.add_argument('-a',
        choices=['change', 'add', 'remove', 'change-line'],
        help="Select action")

    parser.add_argument('-dep',
        type=str,
        help="Dependency name")

    parser.add_argument('-ver',
        type=str,
        help="Version of dependency")

    parser.add_argument('-old',
        type=str,
        help="Old line")

    parser.add_argument('-new',
        type=str,
        help="New line")

    arguments = parser.parse_args()

    path = arguments.path
    action = arguments.a
    dependency = arguments.dep
    version = arguments.ver
    old = arguments.old
    new = arguments.new

    a = ManipulateToml(path, action, dependency, version, old, new)

    a.make_action()

    if action in ['change', 'add', 'remove']:
        a.dump_to_file()
