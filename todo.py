import os

# file to store to do list
TODO_FILE = 'todo-list.txt'

# Load the todo list from a file
def load_todos():
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE, 'w') as file:
            pass
        print(f"{TODO_FILE} created!")
        return []
    with open(TODO_FILE, 'r') as file:
        todos = [line.strip() for line in file.readlines()]
    return todos

# Save the todo list to a file.
def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        for todo in todos:
            file.write(f"{todo}\n")

# Display the current to do list 
def show_todos(todos):
    if not todos:
        print("\nNo tasks in the to-do list.\n")
    else:
        print("\nTo-Do List:")
        for index, todo in enumerate(todos, 1):
            print(f"{index}.{todo}")
    print()

# Add a new Task in to do list 
def add_todo():
    task = input("Enter the new task: ").strip()
    if task:
        todos.append(task)
        save_todos(todos)
        print(f"Task '{task}' added.\n")
    else:
         print("Task cannot be empty!\n")

# Edit an existing task.
def edit_todo():
    show_todos(todos)
    try:
        index = int(input("Enter the task number to edit: ").strip()) -1
        if 0 <= index < len(todos):
            new_task = input(f"Enter the new task for '{todos[index]}': ").strip()
            if new_task:
                todos[index] = new_task
                save_todos(todos)
                print(f"Task updated to '{new_task}'.\n")
            else:
                print("Task cannot be empty!\n")
        else:
           print("Invalid task number.\n") 
    except:
        print("Please enter a valid number.\n")

# Delete a task from the list.
def delete_todo():
    show_todos(todos)
    try:
        index = int(input("Enter the task number to delete: ").strip()) -1
        if 0 <= index < len(todos):
            task = todos.pop(index)
            save_todos(todos)
            print(f"Task '{task}' deleted.\n")
        else:
            print("Invalid task number.\n")
    except:
        print("Please enter a valid number.\n")


# Display the menu and handle user input.
def main_menu():
    while True:
        print("1. View To-Do List")
        print("2. Add a Task")
        print("3. Edit a Task")
        print("4. Delete a Task")
        print("5. Exit")
        try:
            choice = int(input("Choose an option: ").strip())
            match choice:
                case 1:
                    show_todos(todos)
                case 2:
                    add_todo()
                case 3:
                    edit_todo()
                case 4:
                    delete_todo()
                case 5:
                    print("Exiting the To-Do app. Goodbye!")
                    break
        except:
            print("Invalid command! Exiting the To-Do app. Goodbye!")
            break


if __name__ == "__main__":
    todos = load_todos()
    main_menu()