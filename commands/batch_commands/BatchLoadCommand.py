from commands.BatchCommands import BatchCommands
from data import batch_dict


class BatchLoadCoammnd(BatchCommands):
    def __init__(self, cmd):
        super().__init__()
        if len(cmd) != 2 and len(cmd) != 4:
            raise ValueError
        try:
            index = -cmd[1][::-1].index('.')
            self.file_name = cmd[1]
            self.name = cmd[1][:index]
        except:
            self.file_name = cmd[1] + '.dnabatch'
            self.name = cmd[1]
        if len(cmd) == 4:
            if cmd[3][0] != '@':
                raise ValueError
            else:
                self.name = cmd[3][1:]
        if self.name in batch_dict.keys():
            print("Batch is already exist")

    def execute(self):
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()
            batch_dict[self.name] = {}
            for i in range(len(lines)):
                if lines[i].endswith('\n'):
                    lines[i] = lines[i][:-1]
                batch_dict[self.name][len(batch_dict[self.name])] = lines[i]
        except(Exception) as e:
            raise e


    def print_str(self):
        pass