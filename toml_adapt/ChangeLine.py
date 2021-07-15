import toml
import fileinput
import sys

class ChangeLine():
    def __init__(self, path, action, old_line, new_line):
        self.path = path
        self.action = action
        self.old_line = old_line
        self.new_line = new_line

    def change_line(self):
        with fileinput.FileInput(self.path, inplace = True, backup ='.bak') as f:
            for line in f:
                if self.old_line + '\n' == line:
                    print(self.new_line, end ='\n')
                else:
                    print(line, end ='')
