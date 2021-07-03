import toml
import fileinput
import sys

class ManipulateToml():
    def __init__(self, path, action, dependency, version, old_line, new_line):
        self.path = path
        self.action = action
        self.dependency = dependency
        self.version = version

        self.toml_manipulations = ['change', 'add', 'remove']
        self.other_manipulations = ['change-line']

        #change line
        self.old_line = old_line
        self.new_line = new_line

        #load file
        if self.action in self.toml_manipulations:
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

    def get_names_of_dependencies(self):
        return list(self.get_dependencies().keys())

    def get_number_of_dependencies(self):
        return len(self.get_dependencies())

    def change_dep_version(self, dependency, version):
        if version == "X":
            version = "*"
        if dependency == "ALL":
            all_deps = self.get_names_of_dependencies()
            for i in range(len(all_deps)):
                self.data['tool'][self.primary_tool]['dependencies'][all_deps[i]] = version
        else:
            self.data['tool'][self.primary_tool]['dependencies'][dependency] = version

    def remove_dep(self, dependency):
        data = self.get_dependencies()
        try:
            data.pop(dependency)
        except KeyError:
            print("Dependency is not present in current dependency list!")

        return data

    def add_dep(self, dependency, version):
        data = self.get_dependencies()
        if version == "X":
            version = "*"

        data[dependency] = version
        return data

    def change_line(self):
        with fileinput.FileInput(self.path, inplace = True, backup ='.bak') as f:
            for line in f:
                if self.old_line + '\n' == line:
                    print(self.new_line, end ='\n')
                else:
                    print(line, end ='')

    def make_action(self):
        if self.action == "change":
            self.change_dep_version(self.dependency, self.version)
        elif self.action == "add":
            self.add_dep(self.dependency, self.version)
        elif self.action == "remove":
            self.remove_dep(self.dependency)
        elif self.action == "change-line":
            self.change_line()

    def dump_to_file(self):
        with open(self.path, "w") as toml_file:
            toml.dump(self.data, toml_file)
