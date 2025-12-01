import csv
import random
import copy
from galaxy import Galaxy
from heap import MaxHeap
import time

def parse_galaxies(filepath):
    with open(filepath, mode = 'r') as file:
        # Skip the first 12 lines containing metadata
        for row in range(13):
            next(file)

        csvFile = csv.reader(file)

        # Stores galaxy objects
        galaxies = []
        # Dictionary storing id as key and index in galaxies list as value. Helper for filling galaxies list.
        id_index = {}

        # Read csv file and create galaxy objects
        invalid_count = 0
        for row in csvFile:
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

    return galaxies

def quickselect(arr, k):
    arr_copy = copy.deepcopy(arr)

    if k <= 0:
        return []

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

    select(0, len(arr_copy) - 1, k - 1)

    return sorted(arr_copy[:k], key=lambda g: g.distance)

def heap_choose(galaxies, k): # returns function run time
    start = time.time()
    closest_heap = MaxHeap(k)
    closest_heap.insert_first_k(galaxies[0:k])
    for galaxy in galaxies[k:]:
        closest_heap.insert_node(galaxy)
    heap_result = closest_heap.return_all_nodes()
    return heap_result