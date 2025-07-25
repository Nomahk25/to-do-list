import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    if not os.path.exists(TASKS_FILE):
        return []
    with open(TASKS_FILE, 'r') as file:
        return [line.strip() for line in file.readlines()]

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(task + '\n')

def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"✅ Task added: {task}")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("📭 No tasks yet.")
    else:
        print("📝 Your To-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Task removed: {removed}")
    else:
        print("❌ Invalid task number.")

def main():
    while True:
        print("\n=== TO-DO LIST ===")
        print("1. View tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            view_tasks()
        elif choice == '2':
            task = input("Enter task: ")
            add_task(task)
        elif choice == '3':
            view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("❗ Please enter a valid number.")
        elif choice == '4':
            print("👋 Goodbye!")
            break
        else:
            print("❗ Invalid option. Try again.")

if __name__ == "__main__":
    main()
