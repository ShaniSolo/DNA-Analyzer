from data import Dna_sequences_id


class DnaSequence:
    def __init__(self, seq, name):
        if type(seq) is not str or type(name) is not str:
            raise TypeError
        if not self.validate(seq):
            raise ValueError
        self.__sequence = seq
        self.__name = name
        self.__id = len(Dna_sequences_id) + 1

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_seq(self):
        return self.__sequence

    def set_seq(self, new_seq):
        self.__sequence = new_seq

    def set_name(self, new_name):
        self.__name = new_name

    def print_seq(self):
        if len(self.__sequence) <= 40:
            return self.__sequence
        return self.__sequence[:33] + '...' + self.__sequence[len(self.__sequence) - 3:]

    def validate(self, string):
        return all(char in 'ACGT' for char in string)

    def get_sequence(self):
        return self.__sequence

    def insert(self, nucleotide, index):
        if type(index) is not int or type(nucleotide) is not str:
            raise TypeError
        if index > len(self.__sequence):
            raise IndexError
        else:
            self.__sequence = self.__sequence[:index] + nucleotide + self.__sequence[index:]

    def assignment(self, new_sequence):
        if type(new_sequence) is str:
            if not self.validate(new_sequence):
                raise ValueError
            self.__sequence = new_sequence
        elif type(new_sequence) is DnaSequence:
            self.__sequence = new_sequence.get_seq
        else:
            raise TypeError

    def __str__(self):
        return self.__sequence

    def __eq__(self, other):
        if type(other) is not DnaSequence:
            raise TypeError
        else:
            return (self.__sequence == other.get_seq())

    def __ne__(self, other):
        if type(other) is not DnaSequence:
            raise TypeError
        return (self.__sequence != other.get_seq())

    def __getitem__(self, item):
        if type(item) is not int:
            raise TypeError
        if item > len(self.__sequence):
            raise IndexError
        else:
            return self.__sequence[item]

    def __setitem__(self, key, value):
        if type(key) is not int:
            raise TypeError
        if type(value) is not str:
            raise TypeError
        if not self.validate(value):
            raise ValueError
        if key > len(self.__sequence):
            raise IndexError
        else:
            self.__sequence = self.__sequence[:key] + value + self.__sequence[key + 1:]

    def __len__(self):
        return len(self.__sequence)
