from toml_adapt.DocumentOperations import DocumentOperationsEnum
from toml_adapt.DocumentType import DocumentTypeEnum
from toml_adapt.Match import FindMatch
from toml_adapt.AllShapes import all_shapes
from toml_adapt.Shape import Shape
from toml_adapt.ToolExtraction import IsFileCargo, IsFileFlit, IsFileJuliaPkg, IsFilePoetry

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
