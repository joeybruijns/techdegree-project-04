from utilities import clear_screen


def get_name():
    """Collects user name"""
    clear_screen()
    while True:
        name = input("Add Name: ")
        if name == "":
            print("Please, Add Your Name!")
        else:
            break
    return name


def get_task():
    """Collects task name"""
    clear_screen()
    while True:
        task = input("Add Task Name: ")
        if task == "":
            print("Please, Add Task Name!")
        else:
            break
    return task


def get_time():
    """Collects time in minutes"""
    clear_screen()
    while True:
        try:
            time = int(input("Add Time in Minutes: "))
            break
        except ValueError:
            print("Please, Enter a Whole Number in Minutes!")
    return time


def get_notes():
    """Collects optional notes"""
    clear_screen()
    notes = input("Add Notes: (Press <Enter> to Skip) ")
    return notes
