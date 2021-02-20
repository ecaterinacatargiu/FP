class ValidatorException(Exception):

    def __init__(self, messageList=["Validation error!!"]):
        self._messageList = messageList

    @property
    def getmessages(self):
        return self._messageList

    def __str__(self):
        result= ""
        for i in self.getmessages:
            result += i
            result += "\n"
        return result


