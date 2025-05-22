import datetime

tasks = []

# add a task
def add_task(task_name):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    tasks.append({"task": task_name, "timestamp": timestamp, "completed": False})
    print(f"Task '{task_name}' added successfully!")

# view all tasks
def view_tasks():
    if not tasks:
        print("No tasks to display.")
        return
    for index, task in enumerate(tasks, 1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} - {status} (Added on: {task['timestamp']})")

# mark a task as completed
def complete_task(task_number):
    try:
        task = tasks[task_number - 1]
        if not task["completed"]:
            task["completed"] = True
            print(f"Task '{task['task']}' marked as completed!")
        else:
            print(f"Task '{task['task']}' is already completed.")
    except IndexError:
        print("No task is pending")

# menu
def main():
    while True:
        print("\nTo-Do List App")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            task_name = input("Enter task description: ")
            add_task(task_name)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            try:
                task_number = int(input("Enter task number to mark as completed: "))
                complete_task(task_number)
            except ValueError:
                print("Please enter a valid number.")
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()