from commands.AnalysisCommands import AnalysisCommands


class LenCommand(AnalysisCommands):
    def __init__(self, cmd):
        if len(cmd) != 2:
            raise ValueError
        self.seq = self.find_by_key(cmd[1])

    def execute(self):
        self.len = len(self.seq)

    def print_str(self):
        return self.len
