class Lifestyle_Master_Plan:
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            with open(filepath, 'r') as file:
                content = file.read()
                self.plan = {}
                if content:
                    for line in content.split('\n'):
                        if line.strip() and ':' in line:
                            key, value = line.split(':', 1)
                            self.plan[key.strip()] = value.strip()
        except FileNotFoundError:
            self.plan = {
                'Location': '',
                'Work/School': '',
                'Hobbies': ''
            }
    
    def set_value(self, key, value):
        self.plan[key] = value
    
    def get_value(self, key):
        return self.plan.get(key, "Not set")
    
    def add_category(self, category):
        if category not in self.plan:
            self.plan[category] = ''
        else:
            print(f"Category '{category}' already exists")
    
    def remove_category(self, category):
        if category in self.plan:
            del self.plan[category]
        else:
            print(f"Category '{category}' not found")
    
    def view_plan(self):
        print("\n=== LIFESTYLE MASTER PLAN (5-10 Years) ===")
        for key, value in self.plan.items():
            print(f"{key}: {value if value else '[Not set]'}")
        print("=" * 43)
    
    def clear_all(self):
        for key in self.plan:
            self.plan[key] = ''
    
    def __del__(self):
        with open(self.filepath, 'w') as file:
            for key, value in self.plan.items():
                file.write(f"{key}: {value}\n")