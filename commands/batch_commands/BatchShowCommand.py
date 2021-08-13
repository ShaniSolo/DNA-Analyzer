from commands.BatchCommands import BatchCommands
from data import batch_dict


class BatchShowCommand(BatchCommands):
    def __init__(self, cmd):
        if len(cmd) != 2 or cmd[1][0] != '@':
            raise ValueError
        self.name = cmd[1][1:]
        self.commands = None

    def execute(self):
        self.commands = list(batch_dict[self.name].values())

    def print_str(self):
        out = ''
        for i in self.commands:
            out += i + '\n'
        return out[:-1]