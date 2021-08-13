from commands.BatchCommands import BatchCommands
from data import batch_dict


class BatchSaveCommand(BatchCommands):
    def __init__(self, cmd):
        super().__init__()
        if len(cmd) > 3:
            raise ValueError
        if cmd[1][0] != '@':
            raise ValueError
        self.name = cmd[1][1:]
        if len(cmd) == 2:
            try:
                index = -cmd[1][::-1].index('.')
                self.file_name = self.name + '.dnabatch'
            except:
                self.file_name = self.name
        else:
            self.file_name = cmd[2] + '.dnabatch'

    def execute(self):
        out = ''
        for i in list(batch_dict[self.name].values()):
            out += i + '\n'
        try:
            with open(self.file_name, 'a') as file:
                file.write(out[:-1])
        except(Exception) as e:
            raise e

    def print_str(self):
        pass
