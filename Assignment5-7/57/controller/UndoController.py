class UndoController:

    def __init__(self):
        self._operations = []
        self._index = -1
        self._duringUndo = False

    def add(self,operation):
        if self._duringUndo == True:
            return

        self._operations.append(operation)
        self._index = len(self._operations) - 1

    def undo(self):
        if self._index < 0:
            return False

        self._duringUndo = True
        self._operations[self._index].undo()
        self._duringUndo = False
        self._index -=1
        return True

    def redo(self):
        if self._index >=len(self._operations)-1:
            return False

        self._index += 1
        self._duringUndo = True
        self._operations[self._index].redo()
        self._duringUndo = False
        return True


class FunctionCall:

    def __init__(self, functions, *params):
        self._fun = functions
        self._params = params

    def call(self):
        self._fun(*self._params)


class CascadeOperation:

    def __init__(self):
        self._oper = []

    def add(self,operation):
        self._oper.append(operation)

    def undo(self):
        for o in self._oper:
            o.undo()

    def redo(self):
        for o in self._oper:
            o.redo()


class Operation:

    def __init__(self, undoFunction, redoFunction):
        self._undoFunction = undoFunction
        self._redoFunction = redoFunction


    def undo(self):
        self._undoFunction.call()

    def redo(self):
        self._redoFunction.call()