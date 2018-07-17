import sys
import datetime
from collections import OrderedDict

from utilities import clear_screen
from add_entry import get_name, get_task, get_time, get_notes
from search import employee_search, date_search, time_search, search_term

from peewee import *

db = SqliteDatabase("entries.db")


class Entry(Model):
    user_name = CharField(max_length=255)
    task_name = CharField(max_length=255)
    work_time = IntegerField()
    notes = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create database and table if they don't exist"""
    db.connect()
    db.create_tables([Entry], safe=True)


def start_program():
    """Starts the WorkLog Program"""
    clear_screen()
    print("WorkLog | Time Tracking App")
    print("""
    [A] Create New Entry
    [B] Search Entries
    [C] Quit Program
    """)

    while True:
        user_input = input("What Would You Like to Do? ").lower().strip()
        if user_input == "c":
            print("Thank you! Bye!")
            sys.exit()
        elif user_input in main_menu:
            clear_screen()
            main_menu[user_input]()
        else:
            print("Enter A, B or C..")


def new_entry():
    """Collects input and adds it to the database"""
    Entry.create(user_name=get_name(), task_name=get_task(),
                 work_time=get_time(), notes=get_notes())
    input("Entry Saved! Press <Enter> to Return to the Menu ")
    start_program()


def search_entries():
    """Search for existing entries in the database"""
    clear_screen()
    entries = Entry.select().order_by(Entry.timestamp.desc())
    print("Search All Entries:")
    print("""
    [A] Search for Employee
    [B] Search by Date
    [C] Search by Time Spent
    [D] Use a Search Term
    [E] Return to Main Menu
    """)

    while True:
        user_input = input("How Would You Like to Search? ").lower().strip()
        if user_input == "e":
            clear_screen()
            start_program()
        elif user_input in sub_menu:
            clear_screen()
            sub_menu[user_input](entries)
            new_search()
        else:
            print("Please, Try Again!")


def new_search():
    """Asks user what to do next"""
    while True:
        user_input = input("[S]earch More | [R]eturn to Menu ")
        if user_input.upper() == "S":
            search_entries()
        elif user_input.upper() == "R":
            start_program()
        else:
            print("Try again!")


main_menu = OrderedDict([
    ("a", new_entry),
    ("b", search_entries)
])

sub_menu = OrderedDict([
    ("a", employee_search),
    ("b", date_search),
    ("c", time_search),
    ("d", search_term)
])


if __name__ == "__main__":
    initialize()
    start_program()
