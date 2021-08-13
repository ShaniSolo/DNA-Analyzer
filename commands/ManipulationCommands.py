from Command import Command
from DnaSequence import DnaSequence
from data import Dna_sequences_id, Dna_sequences_name


class ManipulationCommands(Command):
    def __init__(self, command):
        try:
            super().__init__(DnaSequence(command[1], command[2][1:]))
        except(TypeError, ValueError, IndexError) as e:
            raise e

    def print_str(self):
        return f'[{self.get_dna().get_id()}] {self.get_dna().get_name()}: {self.get_dna().print_seq()}'

    def validate_input(self, cmd, n1, n2):
        if len(cmd) != n1 and len(cmd) != n2:
            raise ValueError
        if cmd[1][0] != '@':
            if cmd[1][0] != '#':
                raise ValueError
            try:
                int(cmd[1][1:])
            except:
                raise ValueError

    def create_name(self, cmd_list, n1, basic_name):
        try:
            if cmd_list[n1] != ":":
                raise ValueError
            if cmd_list[n1 + 1] == '@@':
                self.new_name(basic_name)
            elif cmd_list[n1 + 1][0] == '@':
                name_new_seq = cmd_list[n1 + 1][1:]
            else:
                raise ValueError
            return name_new_seq
        except:
            return None
