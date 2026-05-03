class Semesterly_Goals:
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            with open(filepath, 'r') as file:
                self.to_do_list = file.read().split('\n')
                # Remove empty strings from the list
                self.to_do_list = [task for task in self.to_do_list if task.strip()]
        except FileNotFoundError:
            self.to_do_list = []
        self.progress = ''
        
    def new_task(self):
        task = input("What would you like to add: ")
        self.to_do_list.append(task)

    def task_completed(self, index):
        self.to_do_list[index-1] += " - Completed"
    
    def remove_task(self, index):
        self.to_do_list.pop(index-1)
    
    def add_progress(self, new_progress):
        self.progress += new_progress
    
    def clear_list(self):
        self.to_do_list = []
    
    def __del__(self): # Saves list to file when program ends
        with open(self.filepath, 'w') as file:
            for x in self.to_do_list:
                file.write(f"{x}\n")
            
        