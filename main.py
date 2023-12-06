# Function to display the to-do list
def display_tasks(tasks):
    if not tasks:
        print("Your to-do list is empty!")
    else:
        print("Your To-Do List:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

# Function to add a task to the to-do list
def add_task(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print("Task added successfully!")

# Function to mark a task as completed
def complete_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number you've completed: ")) - 1
    if 0 <= task_num < len(tasks):
        print(f"Completed task: {tasks[task_num]}")
        tasks.pop(task_num)
    else:
        print("Invalid task number!")

# Function to remove a task from the to-do list
def remove_task(tasks):
    display_tasks(tasks)
    task_num = int(input("Enter the task number you want to remove: ")) - 1
    if 0 <= task_num < len(tasks):
        print(f"Removed task: {tasks[task_num]}")
        tasks.pop(task_num)
    else:
        print("Invalid task number!")

# Main function to run the To-Do List app
def main():
    tasks = []
    while True:
        print("\n===== To-Do List Menu =====")
        print("1. View To-Do List")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Remove Task")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            complete_task(tasks)
        elif choice == '4':
            remove_task(tasks)
        elif choice == '5':
            print("Thank you for using the To-Do List app!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()

