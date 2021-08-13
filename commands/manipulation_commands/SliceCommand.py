from commands.ManipulationCommands import ManipulationCommands
from data import Dna_sequences_id, Dna_sequences_name


class SliceCommand(ManipulationCommands):
    def __init__(self, cmd_list):
        try:
            self.cmd_list = cmd_list
            self.dna = self.find_by_key(self.cmd_list[1])
            basic_name = self.dna.get_name() + '_s' + str(0)
            self.name_new_seq = self.create_name(self.cmd_list, 4, basic_name)
            self.seq = self.dna.get_seq()[int(self.cmd_list[2]):int(self.cmd_list[3])]
            self.validate_input(self.cmd_list, 4, 6)
            int(self.cmd_list[2])
            int(self.cmd_list[3])
        except(Exception) as e:
            raise e

    def execute(self):
        if len(self.cmd_list) == 6:
            s = ['new', self.seq, '@' + self.name_new_seq]
            super().__init__(s)
        else:
            self.dna.set_seq(self.seq)
            Dna_sequences_id[f'{self.dna.get_id()}'] = self.dna
            Dna_sequences_name[self.dna.get_name()] = self.dna

    def print_str(self):
        pass
