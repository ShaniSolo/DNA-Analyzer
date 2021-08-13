from commands.BatchCommands import BatchCommands
# from BatchFactory import BatchFactory
from data import batch_dict


class BatchCreateCommand(BatchCommands):
    def __init__(self, cmd):
        if len(cmd) != 2:
            raise ValueError
        self.cmd = cmd

    def execute(self):
        batch_name = self.cmd[1]
        if batch_name not in batch_dict.keys():
            batch_dict[batch_name] = {}
            read_command = str(input("> batch >>> "))
            while read_command != "end":
                try:
                    batch_dict[batch_name][len(batch_dict[batch_name])] = read_command
                    read_command = str(input("> batch >>> "))
                except(Exception) as e:
                    raise e
        else:
            print("Batch is already exist")
