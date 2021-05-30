import toml

class ManipulateToml():
    def __init__(self, path, action, dependency, version):
        self.path = path
        self.action = action
        self.dependency = dependency
        self.version = version
        #load toml file
        self.data = toml.load(self.path)

        self.tools = []
        self.get_tools()
        self.project_name = self.get_project_name()
        self.primary_tool = self.get_primary_tool()

    def get_project_name(self):
        #for poetry
        if "poetry" in self.tools:
            return self.data['tool']['poetry']['name']

    def get_primary_tool(self):
        if "poetry" in self.tools:
            return "poetry"

    def get_tools(self):
        for key, val in self.data.items():
            for k, v in val.items():
                self.tools.append(k)

    def get_dependencies(self):
        return (self.data['tool'][self.primary_tool]['dependencies'])

    def change_dep_version(self, dependency, version):
        self.data['tool'][self.primary_tool]['dependencies'][dependency] = version

    def remove_dep(self, dependency):
        data = self.get_dependencies()
        try:
            data.pop(dependency)
        except KeyError:
            print("Dependency is not present in dependencies")

        return data

    def add_dep(self, dependency, version):
        data = self.get_dependencies()
        data[dependency] = version
        return data

    def make_action(self):
        if self.action == "change":
            self.change_dep_version(self.dependency, self.version)
        elif self.action == "add":
            self.add_dep(self.dependency, self.version)
        elif self.action == "remove":
            self.remove_dep(dependency)

    def dump_to_file(self):
        output_file_name = "rez/pyproject.toml"
        with open(output_file_name, "w") as toml_file:
            toml.dump(self.data, toml_file)
