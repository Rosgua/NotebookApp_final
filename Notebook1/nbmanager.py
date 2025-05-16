
from notebook import Notebook

class NotebookNotAvailable(Exception):
    pass

class NotebookManager:
    def __init__(self):
        self._notebooks = []
        self._active = None
    
    def getActiveNotebook(self):
        try:
            return self._notebooks[self._active][0]
        except:
            raise NotebookNotAvailable
    
    def getActiveNotebookName(self):
        try:
            return self._notebooks[self._active][1]
        except:
            return "<empty>"
    
    def setActiveNotebook(self, id):
        if id < 0 or id > len(self._notebooks) - 1:
            raise NotebookNotAvailable
        else:
            self._active = id

    def addNotebook(self, name):
        elem = (Notebook(), name)
        self._notebooks.append(elem)
    
    def removeActiveNotebook(self):
        try:
            self._notebooks.pop(self._active)
            self._active = None
        except:
            raise NotebookNotAvailable
        
    def listAvailableNotebooks(self):
        res = []
        for i, e in zip(range(len(self._notebooks)), self._notebooks):
            res.append(str(i)+" "+e[1])
        return res