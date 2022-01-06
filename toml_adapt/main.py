from DocumentOperations import DocumentOperationsEnum
from ManipulateToml import DoOperation

operation: DocumentOperationsEnum=DocumentOperationsEnum.REMOVE

DoOperation(operation,
            toml_file_path="examples/Cargo.toml",
            dependency_name="testing777",
            dependency_version="1.1.1")

DoOperation(operation,
            toml_file_path="examples/poetry_pyproject.toml",
            dependency_name="testing777",
            dependency_version="1.1.1")

DoOperation(operation,
            toml_file_path="examples/flit_pyproject.toml",
            dependency_name="testing777",
            dependency_version="1.1.1")