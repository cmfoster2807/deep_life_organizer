import os
from semesterly_goals import Semesterly_Goals
from lifestyle_plan import Lifestyle_Master_Plan

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def main():
    print("=" * 50)
    print("GOAL MANAGEMENT SYSTEM")
    print("=" * 50)
    
    while True:
        print("\nWhich planner would you like to use?")
        print("1. Semesterly Goals (To-Do List)")
        print("2. Lifestyle Master Plan (5-10 Year Vision)")
        print("3. Exit")
        
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == '1':
            semesterly_menu()
        elif choice == '2':
            lifestyle_menu()
        elif choice == '3':
            print("\nGoodbye! Your progress has been saved.")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

def semesterly_menu():
    filepath = input("\nEnter filepath for semesterly goals (or press Enter for 'goals.txt'): ").strip()
    if not filepath:
        filepath = os.path.join(SCRIPT_DIR, 'goals.txt')    
    
    goals = Semesterly_Goals(filepath)
    
    while True:
        print("\n" + "=" * 50)
        print("SEMESTERLY GOALS")
        print("=" * 50)
        print("\nCurrent Tasks:")
        for i, task in enumerate(goals.to_do_list, 1):
            print(f"{i}. {task}")
        
        print("\nOptions:")
        print("1. Add new task")
        print("2. Mark task as completed")
        print("3. Remove task")
        print("4. Add progress note")
        print("5. View progress notes")
        print("6. Clear all tasks")
        print("7. Back to main menu")
        
        choice = input("\nEnter choice (1-7): ").strip()
        
        if choice == '1':
            goals.new_task()
       
        elif choice == '2':
            try:
                index = int(input("Enter task number to mark complete: "))
                goals.task_completed(index)
                print("Task marked as completed!")
            except (ValueError, IndexError):
                print("Invalid task number.")
        
        elif choice == '3':
            try:
                index = int(input("Enter task number to remove: "))
                goals.remove_task(index)
                print("Task removed!")
            except (ValueError, IndexError):
                print("Invalid task number.")
        
        elif choice == '4':
            note = input("Enter progress note: ")
            goals.add_progress(note + "\n")
            print("Progress note added!")
        
        elif choice == '5':
            print("\n--- Progress Notes ---")
            print(goals.progress if goals.progress else "No progress notes yet.")
        
        elif choice == '6':
            confirm = input("Are you sure you want to clear all tasks? (yes/no): ")
            if confirm.lower() == 'yes':
                goals.clear_list()
                print("All tasks cleared!")
        
        elif choice == '7':
            break
        else:
            print("Invalid choice. Please enter 1-7.")

def lifestyle_menu():
    filepath = input("\nEnter filepath for lifestyle plan (or press Enter for 'lifestyle.txt'): ").strip()
    if not filepath:
        filepath = os.path.join(SCRIPT_DIR, 'lifestyle.txt')
    
    plan = Lifestyle_Master_Plan(filepath)
    
    while True:
        print("\n" + "=" * 50)
        print("LIFESTYLE MASTER PLAN (5-10 Years)")
        print("=" * 50)
        
        plan.view_plan()
        
        print("\nOptions:")
        print("1. Set/Update a value")
        print("2. Add new category")
        print("3. Remove category")
        print("4. View specific value")
        print("5. Clear all values")
        print("6. Back to main menu")
        
        choice = input("\nEnter choice (1-6): ").strip()
        
        if choice == '1':
            key = input("Enter category name: ")
            value = input(f"Enter value for '{key}': ")
            plan.set_value(key, value)
            print(f"'{key}' updated!")
        
        elif choice == '2':
            category = input("Enter new category name: ")
            plan.add_category(category)
            print(f"Category '{category}' added!")
        
        elif choice == '3':
            category = input("Enter category to remove: ")
            plan.remove_category(category)
        
        elif choice == '4':
            key = input("Enter category name: ")
            print(f"\n{key}: {plan.get_value(key)}")
        
        elif choice == '5':
            confirm = input("Are you sure you want to clear all values? (yes/no): ")
            if confirm.lower() == 'yes':
                plan.clear_all()
                print("All values cleared!")
        
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()