from commands.CreationsCommands import CreationCommands
from DnaSequence import DnaSequence


class LoadCommand(CreationCommands):
    '''
    Design pattern: Command
    manage the load command
    '''

    def __init__(self, command):
        try:
            result = self.read_from_file(command)
            cmd = self.validate_input(command)
            if len(command) == 2:
                name = self.new_name(result + '_' + str(0))
            else:
                name = command[2]
            self.dna = DnaSequence(result, name)
        except(Exception) as e:
            raise e

    def read_from_file(self, command):
        file_name = command[1]
        with_prefix = file_name
        if file_name.find(".") == -1:
            with_prefix += ".rawdna"
        try:
            with open(with_prefix, "r") as file:
                seq = file.readline()
            if seq.endswith('\n'):
                seq = seq[:-1]
        except(Exception) as e:
            raise e
        return seq
