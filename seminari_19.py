# 1
# import json
# import csv
# from tabulate import tabulate

# def read_inventory(filename="inventory.json"):
#     try:
#         with open(filename, "r") as file:
#             inventory_data = json.load(file)
#             return inventory_data
#     except FileNotFoundError:
#         print(f"File {filename} does not exist!")
#     except json.decoder.JSONDecodeError:
#         print("Json decoder error. Check your json file!")

# def print_inventory(inventory_data):
#     print(tabulate(inventory_data["items"]))


# inventory_data = read_inventory()
# print_inventory(inventory_data)

import json

def main():
    tasks = load_tasks()

    while True:
        print("Task Manager Menu: ")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Tasks as completed")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            description = input("Enter task description: ")
            add_tasks(tasks, description)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks)
            task_index = int(input("Enter task index: "))
            mark_completed(tasks, task_index)
        elif choice == "4":
            save_tasks(tasks)
            print("Tasks Saved!")
            break
        else:
            print("Invalid choice.")

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except json.decoder.JSONDecodeError:
        tasks = []

    return tasks



def add_tasks(tasks, description):
    task = {"description": description, "completed": False}
    tasks.append(task)
    return tasks

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for element, task in enumerate(tasks, 1):
            print(f"{element}.  {task['description']} - {task['completed']}")

def mark_completed(tasks, task_index):
    tasks[task_index-1]["completed"] = True
    print("Marked as completed!")

def save_tasks(tasks, filename="tasks.json"):
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=2)

if __name__ == "__main__":
    main()

