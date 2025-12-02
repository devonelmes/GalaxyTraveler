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

def main():
    galaxies = parse_galaxies('NED30.5.1-D-17.1.2-20200415.csv')

    window = App()
    window.mainloop()

if __name__ == '__main__':
    main()