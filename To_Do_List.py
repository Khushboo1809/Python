# To-Do List Application


# Function to display the menu
def display_menu():
    print("To-Do List Menu:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Mark a Task as Completed")
    print("4. Remove a Task")
    print("5. Exit")


# Function to view the to-do list
def view_list(todo_list):
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        print("Your To-Do List:")
        for index, task in enumerate(todo_list, start=1):
            print(f"{index}. {task}")


# Function to add a task to the to-do list
def add_task(todo_list):
    task = input("Enter the task to add: ")
    todo_list.append(task)
    print("Task added successfully!")


# Function to mark a task as completed
def mark_completed(todo_list):
    view_list(todo_list)
    if todo_list:
        try:
            index = int(input("Enter the index of the task to mark as completed: "))
            if 1 <= index <= len(todo_list):
                todo_list.pop(index - 1)
                print("Task marked as completed!")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")
    else:
        print("No tasks to mark as completed.")


# Function to remove a task from the to-do list
def remove_task(todo_list):
    view_list(todo_list)
    if todo_list:
        try:
            index = int(input("Enter the index of the task to remove: "))
            if 1 <= index <= len(todo_list):
                todo_list.pop(index - 1)
                print("Task removed successfully!")
            else:
                print("Invalid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")
    else:
        print("No tasks to remove.")


# Main function
def main():
    todo_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            view_list(todo_list)
        elif choice == "2":
            add_task(todo_list)
        elif choice == "3":
            mark_completed(todo_list)
        elif choice == "4":
            remove_task(todo_list)
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


# Run the program
if __name__ == "__main__":
    main()
