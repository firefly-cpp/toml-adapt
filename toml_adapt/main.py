import argparse
import sys
from toml_adapt.ManipulateToml import ManipulateToml
from toml_adapt.ChangeLine import ChangeLine

def start():
    parser = argparse.ArgumentParser(description='Manipulate .toml files')

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
    old_line = arguments.old
    new_line = arguments.new

    toml_manipulations = ['change', 'add', 'remove']
    other_manipulations = ['change-line']

    if action in toml_manipulations:
        a = ManipulateToml(path, action, dependency, version)
        a.make_action()
    elif action in other_manipulations:
        a = ChangeLine(path, action, old_line, new_line)
        a.change_line()

    if action in ['change', 'add', 'remove']:
        a.dump_to_file()
