import requests
import sys
import sqlite3
import argparse
from wrapper import Wrapper
from activity_db import Activity_table

def main():
    if sys.argv[1] == "new":

        # Call a function "parser()" to get access and filter optional comand-line arguments
        args = parser()

        # Call a function "new_activity()" wich return activity value or exit from the program(in case Bored API return error)
        add_to_db = new_activity(args)

        # Create an instance of Activity_table class
        activity_table = Activity_table()

        # Call a classmethod "insert_activity()" wich insert new activity to the database(activity.db)
        Activity_table.insert_activity(add_to_db)

    elif sys.argv[1] == "list":
        # Call a classmethod "latest_activities(n)" wich return the last n activities saved in the database
        print(Activity_table.latest_activities(5))

        Activity_table.conn.close()
    else:
        sys.exit("wrong second command-line argument.")

def parser():
    # Use argparse module to deal with comand-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("Action")
    parser.add_argument("--type")
    parser.add_argument("--participants")
    parser.add_argument("--price_min")
    parser.add_argument("--price_max")
    parser.add_argument("--accessibility_min")
    parser.add_argument("--accessibility_max")

    return parser.parse_args()

def new_activity(cl_arg):
    # Create an instance of Wrapper class
    wrapper = Wrapper(cl_arg.type, cl_arg.participants, cl_arg.price_min, cl_arg.price_max, cl_arg.accessibility_min, cl_arg.accessibility_max)

    # Use try/except. Bored API can return error and trying accesing activity from dictionary will raise a KeyError
    try:
        # Call a get_activity instance method to get an activity
        activity = requests.get(wrapper.get_activity())

        # Use json() method wich allows use Python dictionary and get access to activity value
        return activity.json()["activity"]
    except KeyError:
        sys.exit("error: No activity found with the specified parameters")


if __name__ == "__main__":
    main()


