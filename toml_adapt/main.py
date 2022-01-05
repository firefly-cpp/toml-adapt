#AddDependency("Examples/poetry_pyproject.toml","automatic","9.9.9")
#AddDependency("Examples/Cargo.toml","automatic","9.9.9")
#AddDependency("Examples/flit_pyproject.toml","automatic","9.9.9")

#AddDevDependency("Examples/poetry_pyproject.toml","automatic-dev","9.9.9")
#AddDevDependency("Examples/Cargo.toml","automatic-dev","9.9.9")
#AddDevDependency("Examples/flit_pyproject.toml","automatic-dev","9.9.9")

#RemoveDependency("Examples/poetry_pyproject.toml","automatic")
#RemoveDependency("Examples/Cargo.toml","automatic")
#RemoveDependency("Examples/flit_pyproject.toml","automatic")

#RemoveDevDependency("Examples/poetry_pyproject.toml","automatic-dev")
#RemoveDevDependency("Examples/Cargo.toml","automatic-dev")
#RemoveDevDependency("Examples/flit_pyproject.toml","automatic-dev")

from DocumentOperations import DocumentOperationsEnum
from ManipulateToml import DoOperation

operation: DocumentOperationsEnum=DocumentOperationsEnum.ADD

DoOperation(operation,
            toml_file_path="Examples/Cargo.toml",
            dependency_name="testing777",
            dependency_version="1.1.1")

DoOperation(operation,
            toml_file_path="Examples/poetry_pyproject.toml",
            dependency_name="testing777",
            dependency_version="1.1.1")

DoOperation(operation,
            toml_file_path="Examples/flit_pyproject.toml",
            dependency_name="testing777",
            dependency_version="1.1.1")