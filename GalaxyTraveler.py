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

if __name__ == '__main__':
    main()