from toml_adapt.DocumentOperations import DocumentOperationsEnum
from toml_adapt.ManipulateToml import DoOperation
import click

@click.command()
@click.option('-path',  help='Path to toml file.', required=True)
@click.option('-a',     help='Action. Any of the following: add, remove, change, add-dev, remove-dev, change-dev.', default='change', required=True)      
@click.option('-dep',   help='Dependency name.', required=True)
@click.option('-ver',   help='Dependency version.',   default="1.0.0")
def TomlAdapt(path: str,a: str,dep:str,ver: str):
    operation: DocumentOperationsEnum=DocumentOperationsEnum.CHANGE
    if(a=='add'):
        operation=DocumentOperationsEnum.ADD
    if(a=='remove'):
        operation=DocumentOperationsEnum.REMOVE
    if(a=='change'):
        operation=DocumentOperationsEnum.CHANGE
    if(a=='add-dev'):
        operation=DocumentOperationsEnum.ADD_DEV
    if(a=='remove-dev'):
        operation=DocumentOperationsEnum.REMOVE_DEV
    if(a=='change-dev'):
        operation=DocumentOperationsEnum.CHANGE_DEV
    DoOperation(operation,
                path,
                dep,
                ver)


if __name__ == "__main__":
    TomlAdapt()