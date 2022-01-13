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
        list_of_deps: MutableMapping[str,list[str]]=toml_full_dict["tool"]["flit"]["metadata"]
        if len(list(filter(lambda dep: dependency_name == DependencyNameFromFullString(dep),list_of_deps["requires"]))) > 0:
            print("Dependency already exists")
        else:
            toml_full_dict["tool"]["flit"]["metadata"]["requires"].append(f"{dependency_name} {dependency_version}")
    TomlBaseManipulation(toml_file_path,flit)
    
def RemoveFlitDependency(toml_file_path:str,
                        dependency_name: str):
    """
    [tool.flit.metadata]
    """
    def flit(toml_full_dict: MutableMapping[str,Any]):
        list_of_deps: MutableMapping[str,list[str]]=toml_full_dict["tool"]["flit"]["metadata"]
        list_of_deps["requires"]=list(filter(lambda dep: dependency_name != DependencyNameFromFullString(dep),list_of_deps["requires"]))
    TomlBaseManipulation(toml_file_path,flit)
    
def ChangeFlitDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    """
    [tool.flit.metadata]
    """
    if(dependency_name=="ALL"):
        def flit(toml_full_dict: MutableMapping[str,Any]):
            list_of_deps: MutableMapping[str,list[str]]=toml_full_dict["tool"]["flit"]["metadata"]
            list_of_deps["requires"]=list(map(lambda dep: f"{DependencyNameFromFullString(dep)} {dependency_version}",list_of_deps["requires"]))
        TomlBaseManipulation(toml_file_path,flit)
        return
    def flit(toml_full_dict: MutableMapping[str,Any]):
        list_of_deps: MutableMapping[str,list[str]]=toml_full_dict["tool"]["flit"]["metadata"]
        list_of_deps["requires"]=list(map(lambda dep: f"{dependency_name} {dependency_version}" if dependency_name == DependencyNameFromFullString(dep) else dep,list_of_deps["requires"]))
    TomlBaseManipulation(toml_file_path,flit)
