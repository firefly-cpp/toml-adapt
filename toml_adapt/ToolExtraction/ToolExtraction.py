import pathlib
from typing import Any, Dict, MutableMapping
import toml

def IsSpecificPythonTool(toml_file_path: str, tool_name:str):
    toml_loaded: MutableMapping[str,Any]=toml.load(toml_file_path)
    if(toml_loaded.keys().__contains__("tool")):
        toml_tool: Dict[str,Any]=toml_loaded["tool"]
        if(toml_tool.keys().__contains__(tool_name)):
            return True
    return False

def IsFileFlit(toml_file_path: str) -> bool:
    return IsSpecificPythonTool(toml_file_path,"flit")

def IsFilePoetry(toml_file_path: str) -> bool:
    return IsSpecificPythonTool(toml_file_path,"poetry")

def IsFileCargo(toml_file_path: str) -> bool:
    """
    Cargo requires the file to be named Cargo.toml
    Checking only file path should not be ambiguous
    """
    return pathlib.Path(toml_file_path).name == "Cargo.toml"

def IsFileJuliaPkg(toml_file_path: str) -> bool:
    """
    Julia's pkg tool uses Project.toml file.
    """
    return pathlib.Path(toml_file_path).name == "Project.toml"