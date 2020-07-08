class Error(BaseException): pass


class MyError(Error): 
    def __init__(self,Message,Command):
        self.Command = Command


def main():
    raise MyError("Ошибка в команде",'this')

try:
    main()
except BaseException as Error:
    print(Error.Command)