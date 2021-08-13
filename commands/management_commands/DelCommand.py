from commands.ManagementCommands import ManagementCommands
from data import Dna_sequences_name, Dna_sequences_id


class DelCommand(ManagementCommands):
    def __init__(self, cmd):
        if len(cmd) != 2:
            raise ValueError
        super().__init__(cmd)

    def execute(self):
        print(
            f"do you really want to delete {self.dna.get_name()}: {self.dna.get_seq()}? Please confirm by 'y' "
            f"or 'Y', or cancel by 'n' or 'N'")
        self.ans = input("> confirm >>> ")
        while self.ans not in 'YyNn':
            print("You have typed an invalid response. Please either confirm by 'y'/'Y', or cancel by 'n'/'N'.")
            self.ans = input("> confirm >>>")
        if self.ans in 'Yy':
            id = self.dna.get_id()
            name = self.dna.get_name()
            Dna_sequences_name.pop(name)
            Dna_sequences_id.pop(str(id))

    def print_str(self):
        if self.ans in 'Nn':
            return "Canceled the deleting"
        return f'Deleted: [{self.dna.get_id()}] {self.dna.get_name()}: {self.dna.print_seq()}'
