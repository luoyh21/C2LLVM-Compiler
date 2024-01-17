class SymbolTable:
    def __init__(self):
        self.table = [{}]

    def getItem(self, name):
        currentTable = self.table[-1]
        if name in currentTable:
            return currentTable[name]
        else:
            raise Exception("Variable %s is not declared" % name)
        
    def addItem(self, name, value):
        currentTable = self.table[-1]
        if name in currentTable:
            raise Exception("Duplicate declaration of variable %s" % name)
        else:
            currentTable[name] = value
    
    def push(self):
        self.table.append(self.table[-1].copy())

    def pop(self):
        self.table.pop()