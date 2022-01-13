from typing import Any, MutableMapping

from toml_adapt.Common import TomlBaseManipulation


def AddCargoDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    def cargo(toml_full_dict: MutableMapping[str,Any]):
        toml_full_dict["dependencies"][dependency_name]=f"{dependency_version}"
    TomlBaseManipulation(toml_file_path,cargo)
    
def RemoveCargoDependency(toml_file_path:str,
                        dependency_name: str):
    def cargo(toml_full_dict: MutableMapping[str,Any]):
        toml_full_dict["dependencies"].pop(dependency_name)
    TomlBaseManipulation(toml_file_path,cargo)
    
def ChangeCargoDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    """
    Same as adding
    """
    AddCargoDependency(toml_file_path,dependency_name,dependency_version)
    

def AddCargoDevDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    def cargo(toml_full_dict: MutableMapping[str,Any]):
        toml_full_dict["dev-dependencies"][dependency_name]=f"{dependency_version}"
    TomlBaseManipulation(toml_file_path,cargo)
    
def RemoveCargoDevDependency(toml_file_path:str,
                        dependency_name: str):
    def cargo(toml_full_dict: MutableMapping[str,Any]):
        toml_full_dict["dev-dependencies"].pop(dependency_name)
    TomlBaseManipulation(toml_file_path,cargo)
    
def ChangeCargoDevDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    """
    Same as adding
    """
    AddCargoDevDependency(toml_file_path,dependency_name,dependency_version)
