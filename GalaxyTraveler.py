"""COP3530 Final Project:
✴ Travel Destinations: Nearest Galaxies ✴
Team Name: Galaxy Traveler Trio
Team Members: Devon Elmes, Lang Cao, and Melissa Cote

References:
    https://docs.python.org/3/tutorial/errors.html,
    https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/,
    https://www.geeksforgeeks.org/python/working-csv-files-python/
"""

from ui import App
from helpers import *

WELCOME = "✴✴✴ Welcome, galaxy traveler! ✴✴✴"

MENU = """
========= MENU =========
Please select from the following:
1. Choose how many of the closest galaxies to find.
2. Exit.
========================

Selection: """

DATA_STRUC = """
Which method would you like to use to find the galaxies?
1. Max-heap
2. Quickselect

Selection: """

def main():
    galaxies = parse_galaxies('NED30.5.1-D-17.1.2-20200415.csv')

    window = App()
    window.mainloop()

    # Simple console UI
    while True:
        option = int(input(MENU))
        if option == 1:
            while True:
                # From <peps.python.org/pep-0008/>: "Additionally, for all try/except clauses,
                # limit the try clause to the absolute minimum amount of code necessary."
                try:
                    k = int(input(f"\nPlease enter the number of closest galaxies to find between 1 and {len(galaxies)}: "))
                except ValueError:
                    print("Invalid input.")
                if 1 <= k <= len(galaxies):
                    break
                else:
                    print("Invalid input.")
            while True:
                try:
                    ds = int(input(DATA_STRUC))
                except ValueError:
                    print("Invalid input.")
                if 1 <= ds <= 2:
                    break
                else:
                    print("Invalid input.")
            if ds == 1:
                start = time.time_ns()
                heap_result = heap_choose(galaxies, k)
                end = time.time_ns()
                print("\n✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
                print("\nYou chose Max-heap.")
                print(f"\nThe {k} closest galaxies are: ")
                print()
                for i, galaxy in enumerate(heap_result):
                    galaxy.print_galaxy(i)
                print(f"\nThis method took ~{(end - start)} nanoseconds.")
                print("\n✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
            else:
                start = time.time_ns()
                quick_arr = quickselect(galaxies, k)
                end = time.time_ns()
                print("\n✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
                print("\nYou chose Quickselect.")
                print(f"\nThe {k} closest galaxies are: ")
                print()
                for i, galaxy in enumerate(quick_arr):
                    galaxy.print_galaxy(i)
                print(f"\nThis method took ~{(end - start)} nanoseconds.")
                print("\n✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
                galaxies.clear()
        elif option == 2:
            print("✴ Thank you for using our Galaxy Travel Planner. Have an out-of-this-world day! ✴")
            break
        else:
            print("Invalid selection. Try again.") # We can turn this into a loop if you want, so it keeps prompting.

if __name__ == '__main__':
    main()