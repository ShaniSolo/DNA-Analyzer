from CMDCommand import CMDCommand
from commands.batch_commands.BatchRunCommand import BatchRunCommand


class CLI:
    '''
    execute the cmd
    send the string to CMD Command
    '''

    def __init__(self):
        pass

    def execute(self):
        while True:
            try:
                read_command = str(input("> cmd >>> "))
                if read_command.split()[0] == "run":
                    new_command = BatchRunCommand(read_command)
                else:
                    new_command = CMDCommand(read_command)
                new_command.handler()
            except(Exception) as e:
                # raise e
                print(type(e).__name__)
                pass
