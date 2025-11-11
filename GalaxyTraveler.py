# COP3530 Final Project
# Devon Elmes, Lang Cao, and Melissa Cote
# Let's get this bread
import csv
from Galaxy import Galaxy

if __name__ == '__main__':
    # https://www.geeksforgeeks.org/pandas/reading-csv-files-in-python/
    # https://www.geeksforgeeks.org/python/working-csv-files-python/
    with open('NED30.5.1-D-17.1.2-20200415.csv', mode = 'r') as file:
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













