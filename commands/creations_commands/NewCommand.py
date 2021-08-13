from commands.CreationsCommands import CreationCommands


class NewCommand(CreationCommands):
    '''
    Design pattern: Command
    manage the new command
    '''

    def __init__(self, command):
        try:
            super().__init__(command)
        except(TypeError, ValueError, IndexError) as e:
            raise e
