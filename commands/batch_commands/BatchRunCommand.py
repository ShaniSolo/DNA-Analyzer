from commands.BatchCommands import BatchCommands
from CMDCommand import CMDCommand
from data import batch_dict


class BatchRunCommand(BatchCommands):
    def __init__(self, cmd):
        super().__init__()
        if len(cmd.split()) != 2:
            raise ValueError
        self.cmd = cmd

    def handler(self):
        if self.cmd.split()[1][0] != '@':
            raise ValueError
        batch_name = self.cmd.split()[1][1:]
        for i in range(len(batch_dict[batch_name])):
            new_command = CMDCommand(batch_dict[batch_name][i])
            new_command.handler()
