# Prompt for single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Initialize reminder message
reminder_message = ""

# Process the task based on priority
match priority:
    case "high":
        reminder_message = f"'{task}' is a high priority task"
    case "medium":
        reminder_message = f"'{task}' is a medium priority task"
    case "low":
        reminder_message = f"'{task}' is a low priority task"
    case _:
        reminder_message = "Invalid priority level entered."

# Modify reminder based on time sensitivity
if time_bound == "yes":
    reminder_message += " that requires immediate attention today!"
elif time_bound == "no":
    reminder_message += ". Consider completing it when you have free time."
else:
    # Handle unexpected input for time_bound
    reminder_message += " Invalid response for time sensitivity."

# Print the customized reminder
print(reminder_message)
