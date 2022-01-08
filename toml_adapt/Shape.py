from typing import Callable

from toml_adapt.DocumentType import DocumentTypeEnum

class Shape:
    def __init__(self,
                 document_type: DocumentTypeEnum,
                 add_dependency_function: Callable[[str,str,str],None],
                 remove_dependency_function: Callable[[str,str],None],
                 change_dependency_function: Callable[[str,str,str],None],
                 add_dev_dependency_function: Callable[[str,str,str],None],
                 remove_dev_dependency_function: Callable[[str,str],None],
                 change_dev_dependency_function: Callable[[str,str,str],None]) -> None:
        self.DocumentType: DocumentTypeEnum=document_type
        self.AddDependencyFn: Callable[[str,str,str],None]=add_dependency_function
        self.RemoveDependencyFn: Callable[[str,str],None]=remove_dependency_function
        self.ChangeDependencyFn: Callable[[str,str,str],None]=change_dependency_function
        self.AddDevDependencyFn: Callable[[str,str,str],None]=add_dev_dependency_function
        self.RemoveDevDependencyFn: Callable[[str,str],None]=remove_dev_dependency_function
        self.ChangeDevDependencyFn: Callable[[str,str,str],None]=change_dev_dependency_function
