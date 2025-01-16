from datetime import datetime, timedelta

def display_current_datetime():
    # Get the current date and time
    current_date = datetime.now()
    # Format the current date and time
    formatted_date = current_date.strftime('%Y-%m-%d %H:%M:%S')
    return formatted_date

def calculate_future_date(days):
    # Get the current date
    current_date = datetime.now()
    # Calculate the future date
    future_date = current_date + timedelta(days=days)
    # Format the future date
    formatted_future_date = future_date.strftime('%Y-%m-%d')
    return formatted_future_date

def main():
    # Part 1: Display the Current Date and Time
    current_datetime = display_current_datetime()
    print(f"Current date and time: {current_datetime}")

    # Part 2: Calculate a Future Date
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    future_date = calculate_future_date(days_to_add)
    
    print(f"Future date: {future_date}")

if __name__ == "__main__":
    main()
