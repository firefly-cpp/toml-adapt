from toml_adapt.CargoActions import AddCargoDependency, AddCargoDevDependency, ChangeCargoDependency, ChangeCargoDevDependency, RemoveCargoDependency, RemoveCargoDevDependency
from toml_adapt.DocumentType import DocumentTypeEnum
from toml_adapt.FlitActions import AddFlitDependency, ChangeFlitDependency, RemoveFlitDependency
from toml_adapt.PoetryActions import AddPoetryDependency, AddPoetryDevDependency, ChangePoetryDependency, ChangePoetryDevDependency, RemovePoetryDependency, RemovePoetryDevDependency
from toml_adapt.Shape import Shape

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
