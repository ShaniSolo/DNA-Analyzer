from commands.AnalysisCommands import AnalysisCommands


class FindCommand(AnalysisCommands):
    def __init__(self, string):
        super().__init__(string)

    def execute(self):
        self.index = str(self.seq_to_search).find(str(self.seq_to_find))
