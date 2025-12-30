#!/usr/bin/env python3
"""
CLI Todo Application
Phase 1: In-Memory Python CLI Todo App
"""

# In-memory storage for todos
todos = []
next_id = 1


def add_todo(description):
    """Add a new todo with a unique ID and PENDING status."""
    global next_id
    todo = {
        "id": next_id,
        "description": description,
        "status": "PENDING"
    }
    todos.append(todo)
    next_id += 1
    print(f"Added todo: {description} (ID: {todo['id']})")


def list_todos():
    """Display all todos in a tabular format."""
    if not todos:
        print("\nNo todos found. Your list is empty!")
        return

    print("\nID | Description | Status")
    print("-" * 30)
    for todo in todos:
        print(f"{todo['id']:2} | {todo['description']} | {todo['status']}")


def mark_todo_done(todo_id):
    """Mark a todo as done by its ID."""
    for todo in todos:
        if todo["id"] == todo_id:
            if todo["status"] == "DONE":
                print(f"Todo with ID {todo_id} is already marked as DONE.")
                return
            todo["status"] = "DONE"
            print(f"Marked todo with ID {todo_id} as DONE.")
            return
    
    print(f"Error: Todo with ID {todo_id} does not exist.")


def delete_todo(todo_id):
    """Delete a todo by its ID."""
    global todos
    initial_length = len(todos)
    todos = [todo for todo in todos if todo["id"] != todo_id]
    
    if len(todos) == initial_length:
        print(f"Error: Todo with ID {todo_id} does not exist.")
    else:
        print(f"Deleted todo with ID {todo_id}.")


def display_menu():
    """Display the main menu options."""
    print("\n" + "="*40)
    print("CLI Todo Application")
    print("="*40)
    print("1. Add Todo")
    print("2. List Todos")
    print("3. Mark Todo as Done")
    print("4. Delete Todo")
    print("5. Exit")
    print("-"*40)


def get_user_choice():
    """Get and validate user menu choice."""
    try:
        choice = input("Enter your choice (1-5): ").strip()
        if choice in ["1", "2", "3", "4", "5"]:
            return choice
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")
            return None
    except KeyboardInterrupt:
        print("\n\nExiting application. Goodbye!")
        exit(0)


def handle_add_todo():
    """Handle adding a new todo."""
    description = input("Enter todo description: ").strip()
    if description:
        add_todo(description)
    else:
        print("Error: Description cannot be empty.")


def handle_list_todos():
    """Handle listing all todos."""
    list_todos()


def handle_mark_done():
    """Handle marking a todo as done."""
    try:
        todo_id = int(input("Enter todo ID to mark as done: "))
        mark_todo_done(todo_id)
    except ValueError:
        print("Error: Please enter a valid number for the todo ID.")


def handle_delete():
    """Handle deleting a todo."""
    try:
        todo_id = int(input("Enter todo ID to delete: "))
        delete_todo(todo_id)
    except ValueError:
        print("Error: Please enter a valid number for the todo ID.")


def main():
    """Main application loop."""
    print("Welcome to CLI Todo Application!")
    
    while True:
        display_menu()
        choice = get_user_choice()
        
        if choice == "1":
            handle_add_todo()
        elif choice == "2":
            handle_list_todos()
        elif choice == "3":
            handle_mark_done()
        elif choice == "4":
            handle_delete()
        elif choice == "5":
            print("\nGoodbye! Thanks for using CLI Todo Application.")
            break


if __name__ == "__main__":
    main()