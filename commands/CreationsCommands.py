from Command import Command
from DnaSequence import DnaSequence
from data import Dna_sequences_name


class CreationCommands(Command):
    '''
    Design pattern: Command
    manage the creations commands
    '''
    def __init__(self, cmd):
        try:
            command = self.validate_input(cmd)
            super().__init__(DnaSequence(command[0], command[1]))
        except(Exception) as e:
            raise e

    def validate_input(self, cmd):
        if not 2 <= len(cmd) <= 3:
            raise ValueError
        try:
            seq = cmd[1]
        except(TypeError, ValueError) as e:
            raise e
        if len(cmd) == 3:
            if cmd[2][0] != "@":
                raise ValueError
            name = cmd[2][1:]
        else:
            name = self.new_name('seq0')
        return seq, name

    def print_str(self):
        return f'[{self.dna.get_id()}] {self.dna.get_name()}: {self.dna.print_seq()}'
