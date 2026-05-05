class Semesterly_Goals:
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            with open(filepath, 'r') as file:
                self.to_do_list = file.read().splitlines()  # splitlines() is cleaner than split('\n')
        except FileNotFoundError:
            self.to_do_list = []
        self.progress = ''
        
    def new_task(self):
        task = input("What would you like to add: ")
        self.to_do_list.append(task)
        self.save()

    def task_completed(self, index):
        self.to_do_list[index-1] += " - Completed"
        self.save()
    
    def remove_task(self, index):
        self.to_do_list.pop(index-1)
        self.save()
    
    def add_progress(self, new_progress):
        self.progress += new_progress
        self.save()
    
    def clear_list(self):
        self.to_do_list = []
        self.save()
    
    def save(self):
        with open(self.filepath, 'w') as file:
            for x in self.to_do_list:
                file.write(f"{x}\n")
    
    def __del__(self): # Saves list to file when program ends
        try:
            self.save()
        except:
            pass
        