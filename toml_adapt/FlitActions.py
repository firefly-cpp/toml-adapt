from typing import Any, MutableMapping
from toml_adapt.Common import TomlBaseManipulation

def DependencyNameFromFullString(full_string: str)->str:
    """
    Returns the part without version, only dependency name
    """
    return full_string.split()[0]

def AddFlitDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    """
    [tool.flit.metadata]
    """
    def flit(toml_full_dict: MutableMapping[str,Any]):
        list_of_deps: MutableMapping[str,list[str]]=toml_full_dict["project"]["dependencies"]
        if len(list(filter(lambda dep: dependency_name == DependencyNameFromFullString(dep),list_of_deps))) > 0:
            print("Dependency already exists")
        else:
            if dependency_version == "X":
                toml_full_dict["project"]["dependencies"].append(dependency_name)
            else:
                toml_full_dict["project"]["dependencies"].append(f"{dependency_name} {dependency_version}")
    TomlBaseManipulation(toml_file_path,flit)
    
def RemoveFlitDependency(toml_file_path:str,
                        dependency_name: str):
    """
    [tool.flit.metadata]
    """
    def flit(toml_full_dict: MutableMapping[str,Any]):
        list_of_deps: MutableMapping[str,list[str]]=toml_full_dict["project"]
        list_of_deps["dependencies"]=list(filter(lambda dep: dependency_name != DependencyNameFromFullString(dep),list_of_deps["dependencies"]))
    TomlBaseManipulation(toml_file_path,flit)
    
def ChangeFlitDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    """
    [tool.flit.metadata]
    """
    if(dependency_name=="ALL"):
        def flit(toml_full_dict: MutableMapping[str,Any]):
            list_of_deps: MutableMapping[str,list[str]]=toml_full_dict["project"]["dependencies"]
            list_of_deps["dependencies"]=list(map(lambda dep: DependencyNameFromFullString(dep) if dependency_version == "X" else f"{DependencyNameFromFullString(dep)} {dependency_version}",list_of_deps["dependencies"]))
        TomlBaseManipulation(toml_file_path,flit)
        return
    def flit(toml_full_dict: MutableMapping[str,Any]):
        list_of_deps: MutableMapping[str,list[str]]=toml_full_dict["project"]
        list_of_deps["dependencies"]=list(map(lambda dep: (DependencyNameFromFullString(dep) if dependency_version == "X" else f"{dependency_name} {dependency_version}") if dependency_name == DependencyNameFromFullString(dep) else dep,list_of_deps["dependencies"]))
    TomlBaseManipulation(toml_file_path,flit)
