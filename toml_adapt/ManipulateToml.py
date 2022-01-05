from typing import Any, MutableMapping
from Common import TomlBaseManipulation
from DocumentOperations import DocumentOperationsEnum
from DocumentType import DocumentTypeEnum
from Match import FindMatch
from AllShapes import all_shapes
from Shape import Shape
from ToolExtraction.ToolExtraction import IsFileCargo, IsFileFlit, IsFileJuliaPkg, IsFilePoetry
from FlitActions import AddFlitDependency, RemoveFlitDependency
from PoetryActions import AddPoetryDependency, AddPoetryDevDependency, RemovePoetryDevDependency
from CargoActions import AddCargoDevDependency, RemoveCargoDependency, RemoveCargoDevDependency
from PoetryActions import RemovePoetryDependency

def ExtractTool(toml_file_path: str) -> DocumentTypeEnum:    
    options_list=[
        IsFileFlit(toml_file_path),     DocumentTypeEnum.FLIT,
        IsFilePoetry(toml_file_path),   DocumentTypeEnum.POETRY,
        IsFileCargo(toml_file_path),    DocumentTypeEnum.CARGO,
        IsFileJuliaPkg(toml_file_path), DocumentTypeEnum.JULIAPKG]
    try:
        return FindMatch(options_list,lambda check: check)
    except:
        raise Exception("Invalid document type.")


def AddCargoDependency(toml_file_path:str,
                        dependency_name: str,
                        dependency_version:str):
    def cargo(toml_full_dict: MutableMapping[str,Any]):
        toml_full_dict["dependencies"][dependency_name]=f"{dependency_version}"
    TomlBaseManipulation(toml_file_path,cargo)


    
def AddDependency(toml_file_path: str,
                  dependency_name: str,
                  dependency_version:str) -> None:
    tool_used=ExtractTool(toml_file_path)
    if(tool_used.POETRY):
        AddPoetryDependency(toml_file_path,dependency_name,dependency_version)
    if(tool_used.FLIT):
        AddFlitDependency(toml_file_path,dependency_name,dependency_version)
    if(tool_used.CARGO):
        AddCargoDependency(toml_file_path,dependency_name,dependency_version)
    if(tool_used.JULIAPKG):
        pass # Probably not possible
    
def RemoveDependency(toml_file_path: str,
                  dependency_name: str):
    tool_used=ExtractTool(toml_file_path)
    if(tool_used.POETRY):
        RemovePoetryDependency(toml_file_path,dependency_name)
    if(tool_used.FLIT):
        RemoveFlitDependency(toml_file_path,dependency_name)
    if(tool_used.CARGO):
        RemoveCargoDependency(toml_file_path,dependency_name)
    if(tool_used.JULIAPKG):
        pass # Probably not possible

def AddDevDependency(toml_file_path: str,
                  dependency_name: str,
                  dependency_version:str) -> None:
    tool_used=ExtractTool(toml_file_path)
    if(tool_used.POETRY):
        AddPoetryDevDependency(toml_file_path,dependency_name,dependency_version)
    if(tool_used.FLIT):
        AddFlitDependency(toml_file_path,dependency_name,dependency_version)
    if(tool_used.CARGO):
        AddCargoDevDependency(toml_file_path,dependency_name,dependency_version)
    if(tool_used.JULIAPKG):
        pass # Probably not possible
    
def RemoveDevDependency(toml_file_path: str,
                  dependency_name: str):
    tool_used=ExtractTool(toml_file_path)
    if(tool_used.POETRY):
        RemovePoetryDevDependency(toml_file_path,dependency_name)
    if(tool_used.FLIT):
        RemoveFlitDependency(toml_file_path,dependency_name)
    if(tool_used.CARGO):
        RemoveCargoDevDependency(toml_file_path,dependency_name)
    if(tool_used.JULIAPKG):
        pass # Probably not possible

def GetMatchingShape(toml_file_path:str):
    for shape in all_shapes:
        if(shape.DocumentType == ExtractTool(toml_file_path)):
            return shape
    raise Exception("Document type was not found.")

def DoOperation(
    operation: DocumentOperationsEnum,
    toml_file_path: str = "pyproject.toml",
    dependency_name: str = "",
    dependency_version: str = ""
):
    """
    Operation enum describes what operation should be done.
    Toml file path is relative or absolute path to the toml file that should be manipulated.
    Dependency name is the name of dependency that we wish to work with.
    Dependency version is it's version.
    
    When doing remove operation, the version can (and should) be omitted.
    """
    shape: Shape=GetMatchingShape(toml_file_path)
    if(operation==DocumentOperationsEnum.ADD):
        shape.AddDependencyFn(toml_file_path,dependency_name,dependency_version)
    if(operation==DocumentOperationsEnum.REMOVE):
        shape.RemoveDependencyFn(toml_file_path,dependency_name)
    if(operation==DocumentOperationsEnum.CHANGE):
        shape.ChangeDependencyFn(toml_file_path,dependency_name,dependency_version)
    if(operation==DocumentOperationsEnum.ADD_DEV):
        shape.AddDevDependencyFn(toml_file_path,dependency_name,dependency_version)
    if(operation==DocumentOperationsEnum.REMOVE_DEV):
        shape.RemoveDevDependencyFn(toml_file_path,dependency_name)
    if(operation==DocumentOperationsEnum.CHANGE_DEV):
        shape.ChangeDevDependencyFn(toml_file_path,dependency_name,dependency_version)