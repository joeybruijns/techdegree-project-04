import re

from utilities import clear_screen


def print_entry(value):
    """Prints entry in readable format"""
    timestamp = value.timestamp.strftime("%d/%m/%Y")
    print("-" * len(timestamp))
    print(timestamp)
    print("-" * len(timestamp))
    print("Employee: ", value.user_name)
    print("Task: ", value.task_name)
    print("Time Spent: ", value.work_time)
    print("Notes: ", value.notes + "\n")


def employee_search(data):
    """Search by employee name"""
    clear_screen()
    found = False

    print("All Employees: \n")
    for entry in data:
        print(entry.user_name)

    name = input("\nEnter a Name from the List: ")
    clear_screen()

    for entry in data:
        if name.lower().strip() in entry.user_name.lower():
            print_entry(entry)
            found = True
    if found is False:
        print("Name Not in List..")
    return name


def date_search(data):
    """Search by entry date from timestamp"""
    clear_screen()
    found = False

    print("All Dates: \n")
    for entry in data:
        timestamp = entry.timestamp.strftime("%d/%m/%Y")
        print(timestamp)

    while True:
        input_date = input("\nEnter a Date from the List: ")
        if re.search(r'(\d\d/\d\d/\d\d\d\d)', input_date):
            break
        print("Please, Enter a valid date!")
    clear_screen()

    for entry in data:
        timestamp = entry.timestamp.strftime("%d/%m/%Y")
        if timestamp == input_date:
            print_entry(entry)
            found = True
    if found is False:
        print("No Entries Found..")
    return input_date


def time_search(data):
    """Search by time spent on task"""
    clear_screen()
    found = False

    print("Logged Time Data (Minutes): \n")
    for entry in data:
        print(entry.work_time)

    while True:
        try:
            time = int(input("\nEnter a Time from the List: "))
            break
        except ValueError:
            print("Please, Enter a Valid Number!")
    clear_screen()

    for entry in data:
        if entry.work_time == time:
            print_entry(entry)
            found = True
    if found is False:
        print("No Entries Found..")
    return time


def search_term(data):
    """Use a search term on task name and notes"""
    clear_screen()
    found = False
    user_input = input("Enter a Search Term: ")
    clear_screen()

    for entry in data:
        if user_input.lower().strip() in entry.task_name.lower() \
                or user_input.lower() in entry.notes.lower():
            print_entry(entry)
            found = True
    if found is False:
        print("No Entries Found..")
    return user_input
