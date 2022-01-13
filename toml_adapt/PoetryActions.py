from typing import Any, MutableMapping

from toml_adapt.Common import TomlBaseManipulation


def AddPoetryDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    if dependency_version=="X":
        dependency_version="*"
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
    if dependency_version=="X":
        dependency_version="*"
    if(dependency_name=="ALL"):
        def poetry(toml_full_dict: MutableMapping[str,Any]):
            all_keys: list[str]=toml_full_dict["tool"]["poetry"]["dependencies"].keys()
            for key in all_keys:
                toml_full_dict["tool"]["poetry"]["dependencies"][key]=f"{dependency_version}"
        TomlBaseManipulation(toml_file_path,poetry)
        return
    
    AddPoetryDependency(toml_file_path,dependency_name,dependency_version)
    
def AddPoetryDevDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    if dependency_version=="X":
        dependency_version="*"
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
    if dependency_version=="X":
        dependency_version="*"
    if(dependency_name=="ALL"):
        def poetry(toml_full_dict: MutableMapping[str,Any]):
            all_keys: list[str]=toml_full_dict["tool"]["poetry"]["dev-dependencies"].keys()
            for key in all_keys:
                toml_full_dict["tool"]["poetry"]["dev-dependencies"][key]=f"{dependency_version}"
        TomlBaseManipulation(toml_file_path,poetry)
        return
    AddPoetryDevDependency(toml_file_path,dependency_name,dependency_version)