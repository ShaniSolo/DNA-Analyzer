from data import Dna_sequences_id, Dna_sequences_name


class Command:
    '''
    Interface
    Design pattern: Command
    manage all the commands
    '''

    def __init__(self, obj):
        self.dna = obj

    def get_dna(self):
        return self.dna

    def find_by_key(self, key):
        try:
            if key[0] == '#':
                dna_seq = Dna_sequences_id[key[1:]]
            elif key[0] == '@':
                dna_seq = Dna_sequences_name[key[1:]]
            else:
                raise ValueError
        except(Exception) as e:
            raise e
        return dna_seq

    def new_name(self, name):
        i = 0
        while True:
            i += 1
            name = name[:-1] + str(i)
            if name not in Dna_sequences_name.keys():
                return name

    def execute(self):
        id = str(self.get_dna().get_id())
        name = self.get_dna().get_name()
        if id in Dna_sequences_id.keys() or name in Dna_sequences_name.keys():
            self.get_dna().set_name(self.new_name('seq0'))
        Dna_sequences_id[id] = self.get_dna()
        Dna_sequences_name[name] = self.get_dna()
