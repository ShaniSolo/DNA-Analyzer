from commands.ManipulationCommands import ManipulationCommands


class PairCommand(ManipulationCommands):
    def __init__(self, cmd):
        try:
            self.cmd_list = cmd
            self.validate_input(self.cmd_list, 2, 4)
            self.dna_obj = self.find_by_key(self.cmd_list[1])
        except(Exception) as e:
            raise e

    def execute(self):
        seq = self.dna_obj.get_seq()
        for i in range(len(self.dna_obj)):
            if self.dna_obj[i] == 'T':
                self.dna_obj[i] = 'A'
            elif self.dna_obj[i] == 'A':
                self.dna_obj[i] = 'T'
            elif self.dna_obj[i] == 'C':
                self.dna_obj[i] = 'G'
            else:
                self.dna_obj[i] = 'C'
        basic_name = self.dna_obj.get_name() + '_p' + str(0)
        name_new_seq = self.create_name(self.cmd_list, 2, basic_name)
        if name_new_seq is not None:
            s = ['new',seq, '@' + name_new_seq]
            super().__init__(s)

    def print_str(self):
        return f'[{self.dna_obj.get_id()}] {self.dna_obj.get_name()}: {self.dna_obj.print_seq()}'
