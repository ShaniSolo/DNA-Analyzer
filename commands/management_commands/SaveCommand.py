from commands.ManagementCommands import ManagementCommands


class SaveCommand(ManagementCommands):
    def __init__(self, cmd):
        if not 2 <= len(cmd) <= 3:
            raise ValueError
        super().__init__(cmd)
        if len(cmd) == 3:
            self.file_name = cmd[2] + '.rawdna'
        else:
            self.file_name = self.dna.get_name() + '.rawdna'

    def execute(self):
        try:
            with open(self.file_name, 'a') as file:
                file.write(self.dna.print_seq() + '\n')
        except(Exception) as e:
            raise e

    def print_str(self):
        pass
