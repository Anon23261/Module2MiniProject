import datetime

# List to store tasks
tasks = []

# ANSI escape codes for color coding
RESET_COLOR = "\033[0m"
YELLOW_COLOR = "\033[93m"
GREEN_COLOR = "\033[92m"
RED_COLOR = "\033[91m"

# Function to display the main menu
def show_menu():
    """Displays the main menu options."""
    print("\nWelcome to the To-Do List App!")
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

# Function to add a task
def add_task():
    """Prompts the user to add a new task with title, priority, and due date."""
    task_title = input("Enter the task title: ")

    # Get task priority (High, Medium, Low)
    while True:
        task_priority = input("Enter the task priority (High, Medium, Low): ").capitalize()
        if task_priority in ['High', 'Medium', 'Low']:
            break
        else:
            print("Invalid priority. Please choose High, Medium, or Low.")

    # Get due date in YYYY-MM-DD format
    while True:
        due_date_str = input("Enter the due date (YYYY-MM-DD): ")
        try:
            due_date = datetime.datetime.strptime(due_date_str, '%Y-%m-%d').date()
            break
        except ValueError:
            print("Invalid date format. Please enter a date in YYYY-MM-DD format.")
    
    # Add the task to the list as a dictionary
    tasks.append({
        "title": task_title,
        "status": "Incomplete",   # Default status is 'Incomplete'
        "priority": task_priority,
        "due_date": due_date
    })
    print(f"Task '{task_title}' with priority '{task_priority}' and due date {due_date} added.")

# Function to view all tasks with color coding
def view_tasks():
    """Displays the list of tasks with their statuses, priorities, and due dates."""
    if len(tasks) == 0:
        print("No tasks in the list.")
    else:
        print("\nTo-Do List:")
        today = datetime.date.today()
        for index, task in enumerate(tasks, start=1):
            # Determine color based on task status and due date
            if task['status'] == "Complete":
                color = GREEN_COLOR
            elif task['due_date'] < today:
                color = RED_COLOR  # Overdue tasks are red
            else:
                color = YELLOW_COLOR  # Incomplete tasks are yellow
            
            # Print task with color-coded output
            print(f"{color}{index}. {task['title']} - {task['status']} - Priority: {task['priority']} - Due: {task['due_date']}{RESET_COLOR}")

# Function to mark a task as complete
def mark_task_complete():
    """Marks a selected task as complete."""
    if len(tasks) == 0:
        print("No tasks to mark as complete.")
        return

    try:
        task_number = int(input("Enter the task number to mark as complete: "))
        if 1 <= task_number <= len(tasks):
            tasks[task_number - 1]["status"] = "Complete"
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    """Deletes a selected task from the list."""
    if len(tasks) == 0:
        print("No tasks to delete.")
        return

    try:
        task_number = int(input("Enter the task number to delete: "))
        if 1 <= task_number <= len(tasks):
            deleted_task = tasks.pop(task_number - 1)
            print(f"Task '{deleted_task['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

# Main function to run the application
def main():
    """Main function to handle user input and manage the To-Do list."""
    while True:
        # Display the menu
        show_menu()

        try:
            # Get user input for menu selection
            choice = int(input("\nChoose an option (1-5): "))

            if choice == 1:
                add_task()
            elif choice == 2:
                view_tasks()
            elif choice == 3:
                mark_task_complete()
            elif choice == 4:
                delete_task()
            elif choice == 5:
                print("Exiting the application. Goodbye!")
                break
            else:
                print("Invalid option. Please choose a number between 1 and 5.")

        except ValueError:
            print("Please enter a valid number.")

# Run the application
if __name__ == "__main__":
    main()
