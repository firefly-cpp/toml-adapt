from CargoActions import AddCargoDependency, AddCargoDevDependency, ChangeCargoDependency, ChangeCargoDevDependency, RemoveCargoDependency, RemoveCargoDevDependency
from DocumentType import DocumentTypeEnum
from FlitActions import AddFlitDependency, ChangeFlitDependency, RemoveFlitDependency
from PoetryActions import AddPoetryDependency, AddPoetryDevDependency, ChangePoetryDependency, ChangePoetryDevDependency, RemovePoetryDependency, RemovePoetryDevDependency
from Shape import Shape


all_shapes: list[Shape]=[
    Shape(DocumentTypeEnum.POETRY,
    AddPoetryDependency,
    RemovePoetryDependency,
    ChangePoetryDependency,
    AddPoetryDevDependency,
    RemovePoetryDevDependency,
    ChangePoetryDevDependency)
    ,
    Shape(DocumentTypeEnum.CARGO,
    AddCargoDependency,
    RemoveCargoDependency,
    ChangeCargoDependency,
    AddCargoDevDependency,
    RemoveCargoDevDependency,
    ChangeCargoDevDependency)
    ,
    Shape(DocumentTypeEnum.FLIT,
    AddFlitDependency,
    RemoveFlitDependency,
    ChangeFlitDependency,
    AddFlitDependency,
    RemoveFlitDependency,
    ChangeFlitDependency)
]