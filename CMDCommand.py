from commands.batch_commands.BatchCreateCommand import BatchCreateCommand
from commands.batch_commands.BatchListCommand import BatchListCommand
from commands.batch_commands.BatchLoadCommand import BatchLoadCoammnd
from commands.batch_commands.BatchSaveCommand import BatchSaveCommand
from commands.batch_commands.BatchShowCommand import BatchShowCommand
from commands.analaysis_commands.CountCommand import CountCommand
from commands.management_commands.DelCommand import DelCommand
from commands.creations_commands.DupCommand import DupCommand
from commands.analaysis_commands.FindComand import FindCommand
from commands.analaysis_commands.FindallCommand import FindallCommand
from commands.analaysis_commands.LenCommand import LenCommand
from commands.creations_commands.LoadCommand import LoadCommand
from commands.creations_commands.NewCommand import NewCommand
from commands.manipulation_commands.PairCommand import PairCommand
from commands.management_commands.SaveCommand import SaveCommand
from commands.manipulation_commands.SliceCommand import SliceCommand


class CMDCommand:
    '''
    Design pattern: Factory
    implement the invoker class of the Command design pattern
    check the type of the command and if it valid- create the command object
    save the recived object (here?)
    '''

    def __init__(self, cmd):
        self.cmd = cmd.split()
        self.commands = {
            "new": NewCommand,
            "load": LoadCommand,
            "dup": DupCommand,
            "slice": SliceCommand,
            "pair": PairCommand,
            "del": DelCommand,
            "save": SaveCommand,
            "find": FindCommand,
            "findall": FindallCommand,
            "len": LenCommand,
            "count": CountCommand,
            "batch": BatchCreateCommand,
            "batchlist": BatchListCommand,
            "batchshow": BatchShowCommand,
            "batchsave": BatchSaveCommand,
            "batchload": BatchLoadCoammnd
        }

    def handler(self):
        cmd = self.commands[self.cmd[0]](self.cmd)
        cmd.execute()
        out = cmd.print_str()
        if out is not None:
            print(out)
        return cmd
