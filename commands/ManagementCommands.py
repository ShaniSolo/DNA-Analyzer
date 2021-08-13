from Command import Command


class ManagementCommands(Command):
    def __init__(self, cmd):
        try:
            super().__init__(self.find_by_key(cmd[1]))
        except(Exception) as e:
            raise e