from commands.CreationsCommands import CreationCommands


class DupCommand(CreationCommands):
    '''
    Design pattern: Command
    manage the duplicate command
    '''

    def __init__(self, cmd):
        try:
            if not 2 <= len(cmd) <= 3:
                raise ValueError
            self.dna = self.find_by_key(cmd[1])
            if len(cmd) == 3:
                self.name = cmd[2]
            else:
                self.name = self.new_name('@' + self.dna.get_name() + '_' + str(0))
            s = f'{cmd[0]} {self.dna.get_seq()} @{self.name}'
            super().__init__(s)
        except(Exception) as e:
            raise e

    def validate_input(self, cmd):
        return self.dna.get_seq(), self.name
