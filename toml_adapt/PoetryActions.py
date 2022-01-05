from typing import Any, MutableMapping

from Common import TomlBaseManipulation


def AddPoetryDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    def poetry(toml_full_dict: MutableMapping[str,Any]):
        toml_full_dict["tool"]["poetry"]["dependencies"][dependency_name]=f"{dependency_version}"
    TomlBaseManipulation(toml_file_path,poetry)
    
def RemovePoetryDependency(toml_file_path:str,
                        dependency_name: str):
    def poetry(toml_full_dict: MutableMapping[str,Any]):
        toml_full_dict["tool"]["poetry"]["dependencies"].pop(dependency_name)
    TomlBaseManipulation(toml_file_path,poetry)
    
def ChangePoetryDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    """
    Same as adding
    """
    AddPoetryDependency(toml_file_path,dependency_name,dependency_version)
    
def AddPoetryDevDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    def poetry(toml_full_dict: MutableMapping[str,Any]):
        toml_full_dict["tool"]["poetry"]["dev-dependencies"][dependency_name]=f"{dependency_version}"
    TomlBaseManipulation(toml_file_path,poetry)
    
def RemovePoetryDevDependency(toml_file_path:str,
                        dependency_name: str):
    def poetry(toml_full_dict: MutableMapping[str,Any]):
        toml_full_dict["tool"]["poetry"]["dev-dependencies"].pop(dependency_name)
    TomlBaseManipulation(toml_file_path,poetry)
    
def ChangePoetryDevDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    """
    Same as adding
    """
    AddPoetryDevDependency(toml_file_path,dependency_name,dependency_version)