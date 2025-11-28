"""
COP3530 Final Project: ✴ Travel Destinations: Nearest Galaxies ✴
Team Name: Galaxy Traveler Trio
Team Members: Devon Elmes, Lang Cao, and Melissa Cote

References:
    https://docs.python.org/3/tutorial/errors.html,
    https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/,
    https://www.geeksforgeeks.org/python/working-csv-files-python/
"""

import csv
import random
import copy
import tkinter as tk
import customtkinter as ctk
from galaxy import Galaxy
from heap import MaxHeap

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

# def CreateMenuWindow():
#     ctk.set_appearance_mode("dark")
#     ctk.set_default_color_theme("blue")

#     root = tk.Tk()
#     root.title('✴ Galaxy Traveler ✴')
#     root.geometry('800x500')
#     # Add widgets
#     tk.Label(root, text=WELCOME).pack()
#     tk.Button(root, )
#     return root

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("✴ Galaxy Traveler ✴")
        self.geometry("400x300")

        # Sidebar frame
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.pack(side="left", fill="y")

        # Sidebar buttons
        ctk.CTkLabel(self.sidebar, text="Menu", font=("Helvetica", 18)).pack(pady=20)

        self.btn1 = ctk.CTkButton(self.sidebar, text="Button 1", command=self.say_hi)
        self.btn1.pack(pady=10)

        self.btn2 = ctk.CTkButton(self.sidebar, text="Button 2")
        self.btn2.pack(pady=10)

        # Main content area
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="left", fill="both", expand=True)

        self.label = ctk.CTkLabel(self.main_frame, text="Hello!", font=("Arial", 24))
        self.label.pack(pady=40)

    def say_hi(self):
        self.label.configure(text="Hi 👋")

def parse_galaxies(filepath):
    with open(filepath, mode = 'r') as file:
        # Skip the first 12 lines containing metadata
        for row in range(13):
            next(file)

        csvFile = csv.reader(file)
        seen = set()
        current_id = None
        grouped = True
        line_num = 0

        # Stores galaxy objects
        galaxies = []
        # Dictionary storing id as key and index in galaxies list as value. Helper for filling galaxies list.
        id_index = {}

        # Read csv file and create galaxy objects
        invalid_count = 0
        for i, row in enumerate(csvFile):
            try:
                galaxy_id = row[3] # NED "Preferred Object Name" for the host galaxy
                mm = float(row[4]) # Distance Modulus expressed in mag
                err = float(row[5]) # Quoted (one-sigma) statistical (random) error on the distance modulus
                mpc = float(row[6]) # Metric distance (in units of Mpc)
                if err == 0:
                    raise ValueError("error is 0") # If err == 0, will cause denominator in weighted mean to be 0
                if len(galaxy_id) == 0:
                    raise ValueError("galaxy id is empty")
            except ValueError:
                invalid_count += 1
                continue

            # If galaxy has already been added to galaxies, add information from this row to its data list
            if galaxy_id in id_index:
                galaxies[id_index[galaxy_id]].add_data(mm, err, mpc)
            # Create galaxy if not in list and add its index in galaxies to id_index
            else:
                new_galaxy = Galaxy(galaxy_id)
                new_galaxy.add_data(mm, err, mpc)
                galaxies.append(new_galaxy)
                id_index[galaxy_id] = len(galaxies) - 1

        # Set distances for all galaxies
        for galaxy in galaxies:
            galaxy.set_distance()

        print("Invalid rows in file: " + str(invalid_count))
        print("Galaxies in list: " + str(len(galaxies)))
    return galaxies

def quickselect(arr, k):
    arr_copy = copy.deepcopy(arr)

    if k <= 0:
        return []

    def select(left, right, k_smallest):
        if left == right:
            return

        pivot_index = random.randint(left, right)
        pivot_index = partition(left, right, pivot_index)

        if k_smallest == pivot_index:
            return
        elif k_smallest < pivot_index:
            select(left, pivot_index - 1, k_smallest)
        else:
            select(pivot_index + 1, right, k_smallest)

    def partition(left, right, pivot_index):
        pivot_value = arr_copy[pivot_index].distance
        arr_copy[pivot_index], arr_copy[right] = arr_copy[right], arr_copy[pivot_index]

        store_index = left
        for i in range(left, right):
            if arr_copy[i].distance < pivot_value:
                arr_copy[i], arr_copy[store_index] = arr_copy[store_index], arr_copy[i]
                store_index += 1

        arr_copy[store_index], arr_copy[right] = arr_copy[right], arr_copy[store_index]
        return store_index

    select(0, len(arr_copy) - 1, k - 1)

    return sorted(arr_copy[:k], key=lambda g: g.distance)

def main():
    galaxies = parse_galaxies('NED30.5.1-D-17.1.2-20200415.csv')

    # Create display window
    window = create_menu_window()

    # window.mainloop()
    print(WELCOME)

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
                closest_heap = MaxHeap(k)
                closest_heap.insert_first_k(galaxies[0:k])
                for galaxy in galaxies[k:]:
                    closest_heap.insert_node(galaxy)
                heap_result = closest_heap.return_all_nodes()
                print("\n✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
                print("\nYou chose Max-heap.")
                print(f"The {k} closest galaxies are: ")
                print()
                num = 1
                for galaxy in heap_result:
                    galaxy.print_galaxy(num)
                    num += 1
                print("\n✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
                print(f"\nThis method took {0} nanoseconds.") # need to edit once I set up timer
            else:
                quick_arr = quickselect(galaxies, k)
                print("\n✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
                print("\nYou chose Quickselect.")
                print(f"\nThe {k} closest galaxies are: ")
                print()
                num = 1
                for galaxy in quick_arr:
                    galaxy.print_galaxy(num)
                    num += 1
                print("\n✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴✴")
                print(f"\nThis method took {0} nanoseconds.")  # need to edit once I set up timer
        elif option == 2:
            print("✴ Thank you for using our Galaxy Travel Planner. Have an out-of-this-world day! ✴")
            break
        else:
            print("Invalid selection. Try again.") # We can turn this into a loop if you want, so it keeps prompting.

if __name__ == '__main__':
    main()