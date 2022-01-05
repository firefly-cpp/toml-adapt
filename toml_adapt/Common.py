from typing import Any, Callable, MutableMapping
import toml

def ManipulateFile(toml_file_path:str,
                   new_toml: MutableMapping[Any,Any]):
    try:
        with open(toml_file_path, "w") as file:
            toml.dump(new_toml,file)
    except:
        pass

def TomlBaseManipulation(toml_file_path: str,ManipulationFunction: Callable[[Any],None]):
    try:
        toml_full_dict=toml.load(toml_file_path)
        ManipulationFunction(toml_full_dict)
        ManipulateFile(toml_file_path,toml_full_dict)
    except:
        pass