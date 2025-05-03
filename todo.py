import datetime

FILENAME = "tasks.txt"

def show_tasks():
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
            if tasks:
                print("\nYour Tasks:")
                for i, task in enumerate(tasks, 1):
                    print(f"{i}. {task.strip()}")
            else:
                print("\nNo tasks found.")
    except FileNotFoundError:
        print("\nNo tasks file found yet.")

def add_task():
    task = input("Enter a new task: ")
    priority = input("Priority (High / Medium / Low): ").capitalize()
    deadline = input("Deadline (YYYY-MM-DD): ")

    try:
        datetime.datetime.strptime(deadline, "%Y-%m-%d")  # validate date
    except ValueError:
        print("Invalid date format! Task not added.")
        return

    full_task = f"{task} [Priority: {priority}] [Deadline: {deadline}]"
    with open(FILENAME, "a") as file:
        file.write(full_task + "\n")
    print("Task added.")

def delete_task():
    show_tasks()
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            with open(FILENAME, "w") as file:
                file.writelines(tasks)
            print(f"Deleted: {removed.strip()}")
        else:
            print("Invalid task number.")
    except:
        print("Error deleting task.")

def mark_done():
    show_tasks()
    try:
        with open(FILENAME, "r") as file:
            tasks = file.readlines()
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            if "✅" not in tasks[task_num - 1]:
                tasks[task_num - 1] = "✅ " + tasks[task_num - 1]
                with open(FILENAME, "w") as file:
                    file.writelines(tasks)
                print("Task marked as done.")
            else:
                print("Task is already marked as done.")
        else:
            print("Invalid task number.")
    except:
        print("Error marking task.")

def main():
    while True:
        print("\n--- To-Do List Menu ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task as Done")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            mark_done()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
