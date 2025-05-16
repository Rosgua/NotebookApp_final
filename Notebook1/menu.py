import sys
from notebook import Notebook
from nbmanager import NotebookManager, NotebookNotAvailable

class Menu:
    def __init__(self):
        self.notebook = None
        self.manager = NotebookManager()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.add_note,
            "4": self.modify_note,
            "5": self.quit,
            "6": self.add_notebook,
            "7": self.list_notebooks,
            "8": self.set_notebook,
            "9": self.remove_notebook,
        }

    def display_menu(self):
        print(
               f'''
   Notebook {self.manager.getActiveNotebookName()} Menu

1. Show all Notes
2. Search Notes 
3. Add Note
4. Modify Note
5. Quit
6. Add Notebook
7. List Notebooks
8. Set Active Notebook
9. Remove Active Notebook
'''
        )
        
    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                self.fix(action) # fix
            else:
                print("{0} is not a valid choice".format(choice))

    
    def fix(self, f):
        if self.notebook == None and f in [self.add_note, self.show_notes, self.modify_note, self.search_notes]:
            print("ERROR: notebook empty")
        else:
            f()
                 
 
    def add_notebook(self):
        name = input("Insert notebook name: ")
        self.manager.addNotebook(name)

    
    def list_notebooks(self):
        nbooks = self.manager.listAvailableNotebooks()
        print("")
        for b in nbooks:
            print(b)
        print("")
        
    
    def set_notebook(self):
        ids = input("Insert notebook id:")
        try:
            id = int(ids)
            self.manager.setActiveNotebook(id)
            self.notebook=self.manager.getActiveNotebook()
        except NotebookNotAvailable:
            print("ERROR: notebook not available")
        except Exception:
            print("ERROR: incorrect id format")
        else:
            print(f"Ok: notebook {self.manager.getActiveNotebookName()} ON LINE")
    
   
    def remove_notebook(self):
        try:
            self.manager.removeActiveNotebook()
            self.notebook = None
        except NotebookNotAvailable:
            print("ERROR: notebook not available")
        else:
            print("Ok: notebook REMOVED")
    
    # changed        
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            #print("{0}: {1}\n{2}".format(note.id, note.tags, note.memo))
            note.view()

    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
    
    # changed
    def add_note(self):
        note = None
        category = input("Enter note type (simple, todolist, postit): ")
        memo = input("Enter a memo: ")
        if category == "postit":
            color = input("Select a color: ")
            self.notebook.new_postit(memo, color)
        elif category == "todolist":
            todos = input("Enter a todo list (str,str,...): ")
            ltodos = todos.split(",")
            self.notebook.new_todolist(memo, ltodos)
        elif category == "simple":
            self.notebook.new_note(memo)
        print("Your note has been added.")


    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo:
            self.notebook.modify_memo(id, memo)
        if tags:
            self.notebook.modify_tags(id, tags)

    def quit(self):
        print("Thank you for using your notebook today.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()