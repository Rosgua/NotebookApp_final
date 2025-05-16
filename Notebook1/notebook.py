import datetime
import abc

# changed
class Note(metaclass=abc.ABCMeta):
    # Store the next available id for all new notes
    last_id = 0

    def __init__(self, memo, tags=""):
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        Note.last_id += 1
        self.id = Note.last_id

    def match(self, filter):
        return filter in self.memo or filter in self.tags 

    @abc.abstractmethod
    def view(self):
        pass
    
#new
class SimpleNote(Note):
    def view(self):
        print("***** THIS IS A SIMPLE NOTE *****")
        print(f"NOTE ID: {self.id}")
        print(f"MEMO: {self.memo}")
        print(f"TAGS: {self.tags}")
        print("*********************************")

# new
class PostIt(Note):
    def __init__(self, color, memo, tags):
        super().__init__(memo, tags)
        self.color = color        

    def view(self):
        print(f"***** THIS IS A {self.color} POST-IT *****")
        print(f"NOTE ID: {self.id}")
        print(f"MEMO: {self.memo}")
        print(f"TAGS: {self.tags}")
        print("******************************************")

# new
class ToDo(Note):
    def __init__(self, todos, memo, tags):
        super().__init__(memo, tags)
        self.todos = todos        

    def view(self):
        stodos = ""
        for i, e in zip(range(1,len(self.todos)+1), self.todos):
            stodos = stodos + " " + str(i) + ": " + e
        print("***** THIS IS A TO-DO LIST ******")
        print(f"NOTE ID: {self.id}")
        print(f"MEMO: {self.memo}")
        print(f"TAGS: {self.tags}")
        print(f"TODO: {stodos}")
        print("*********************************")


class Notebook:
    def __init__(self):
        self.notes = []

    # changed
    def new_note(self, memo, tags=""):
        self.notes.append(SimpleNote(memo, tags))
    
    # new
    def new_postit(self, memo, color, tags=""):
        self.notes.append(PostIt(color, memo, tags))
    #new
    def new_todolist(self, memo, todos, tags=""):
        self.notes.append(ToDo(todos, memo, tags))

    # fixed
    def modify_memo(self, note_id, memo):
        for note in self.notes:
            if str(note.id) == str(note_id):
                note.memo = memo
                break
    
    # fixed
    def modify_tags(self, note_id, tags):
        for note in self.notes:
            if str(note.id) == str(note_id):
                note.tags = tags
                break

    def search(self, filter):
        result=[]
        for note in self.notes:
            if note.match(filter):
                result.append(note)
        return result
