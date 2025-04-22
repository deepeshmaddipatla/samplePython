import json
import os

TODO_FILE = 'tasks.json'

def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, 'r') as file:
        return json.load(file)

def save_tasks(tasks):
    with open(TODO_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def show_tasks(tasks):
    if not tasks:
        print("✅ No tasks! You're all caught up.")
        return
    print("\n📋 Your To-Do List:")
    for idx, task in enumerate(tasks, 1):
        status = "✔️" if task['done'] else "❌"
        print(f"{idx}. {status} {task['title']}")

def add_task(title):
    tasks = load_tasks()
    tasks.append({'title': title, 'done': False})
    save_tasks(tasks)
    print(f"➕ Added: {title}")

def mark_done(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]['done'] = True
        save_tasks(tasks)
        print(f"✅ Marked as done: {tasks[index]['title']}")
    else:
        print("⚠️ Invalid task number.")

def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed = tasks.pop(index)
        save_tasks(tasks)
        print(f"🗑️ Deleted: {removed['title']}")
    else:
        print("⚠️ Invalid task number.")

def main():
    while True:
        print("\n🧠 To-Do App")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            show_tasks(load_tasks())
        elif choice == '2':
            title = input("Enter task: ")
            add_task(title)
        elif choice == '3':
            show_tasks(load_tasks())
            try:
                index = int(input("Enter task number to mark as done: ")) - 1
                mark_done(index)
            except ValueError:
                print("⚠️ Enter a valid number.")
        elif choice == '4':
            show_tasks(load_tasks())
            try:
                index = int(input("Enter task number to delete: ")) - 1
                delete_task(index)
            except ValueError:
                print("⚠️ Enter a valid number.")
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

if __name__ == '__main__':
    main()
