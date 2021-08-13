from Command import Command


class AnalysisCommands(Command):
    def __init__(self, cmd):
        if len(cmd) != 3:
            raise ValueError
        self.seq_to_search = self.find_by_key(cmd[1])
        if cmd[2][0] in '#@':
            self.seq_to_find = self.find_by_key(cmd[2])
        else:
            self.seq_to_find = cmd[2]
        self.index = -1

    def execute(self):
        pass


    def print_str(self):
        if self.index != -1:
            return self.index
