"""
To-Do List Application
A simple command-line program that allows users to add, view, and delete tasks.
"""

# Global list to store tasks
tasks = []


def display_menu():
    """Displays the main menu options."""
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Quit")


def add_task():
    """Adds a new task to the list."""
    try:
        task = input("Enter a new task: ").strip()

        if not task:
            raise ValueError("Task cannot be empty.")

        tasks.append(task)
        print(f"Task '{task}' added successfully!")

    except ValueError as e:
        print(f"Error: {e}")

    finally:
        print("Returning to main menu...")


def view_tasks():
    """Displays all tasks in the list."""
    try:
        if not tasks:
            raise IndexError("No tasks available to view.")

        print("\nYour Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

    except IndexError as e:
        print(f"Error: {e}")

    finally:
        print("Returning to main menu...")


def delete_task():
    """Deletes a task based on user input."""
    try:
        if not tasks:
            raise IndexError("No tasks available to delete.")

        view_tasks()

        choice = int(input("Enter the task number to delete: "))

        if choice < 1 or choice > len(tasks):
            raise ValueError("Invalid task number.")

        removed_task = tasks.pop(choice - 1)
        print(f"Task '{removed_task}' deleted successfully!")

    except ValueError:
        print("Error: Please enter a valid number.")

    except IndexError as e:
        print(f"Error: {e}")

    finally:
        print("Returning to main menu...")


def main():
    """Main function to run the To-Do application."""
    print("Welcome to the To-Do List Application!")

    while True:
        display_menu()

        try:
            selection = input("Choose an option (1-4): ").strip()

            if selection not in ["1", "2", "3", "4"]:
                raise ValueError("Invalid menu selection.")

            if selection == "1":
                add_task()
            elif selection == "2":
                view_tasks()
            elif selection == "3":
                delete_task()
            elif selection == "4":
                print("Thank you for using the To-Do List App. Goodbye!")
                break

        except ValueError as e:
            print(f"Error: {e}")

        finally:
            print("-" * 30)


# Run the program
if __name__ == "__main__":
    main()