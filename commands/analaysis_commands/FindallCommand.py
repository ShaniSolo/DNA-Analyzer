from commands.AnalysisCommands import AnalysisCommands


class FindallCommand(AnalysisCommands):
    def __init__(self, string):
        super().__init__(string)

    def execute(self):
        ans = [i for i in range(len(self.seq_to_search) - len(self.seq_to_find) + 1) if str(self.seq_to_search).startswith(str(self.seq_to_find), i)]
        self.index = ""
        for i in ans:
            self.index += str(i) + " "
        if self.index == "":
            self.index = None
        return self.index
