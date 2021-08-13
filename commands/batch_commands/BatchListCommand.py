from commands.BatchCommands import BatchCommands
from data import batch_dict


class BatchListCommand(BatchCommands):
    def __init__(self, cmd):
        self.keys = None

    def execute(self):
        self.keys = list(batch_dict.keys())

    def print_str(self):
        return self.keys