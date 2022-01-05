from typing import Any, MutableMapping
from Common import TomlBaseManipulation

def AddJuliaDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_hash:str):
    def julia(toml_full_dict: MutableMapping[str,Any]):
        toml_full_dict["deps"][dependency_name]=f"{dependency_hash}"
    TomlBaseManipulation(toml_file_path,julia)

def RemoveJuliaDependency(toml_file_path:str,
                        dependency_name: str):
    def julia(toml_full_dict: MutableMapping[str,Any]):
        toml_full_dict["deps"].pop(dependency_name)
    TomlBaseManipulation(toml_file_path,julia)
    
def ChangeJuliaDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    """
    Due to the fact it's a map, it's implemented the same as adding a dependency
    """
    AddJuliaDependency(toml_file_path,dependency_name,dependency_version)