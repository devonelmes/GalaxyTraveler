"""References:

set_distance():
    Measurement of Distances: https://ned.ipac.caltech.edu/level5/Sept11/Freedman/Freedman3.html
    https://en.wikipedia.org/wiki/Distance_modulus
    m - M (distance modulus) = 5 log d - 5. d is parsecs, log base 10
    https://astro.wku.edu/labs/m100/mags.html
    Solve for d to get distance in parsecs: d = 10 ** (0.2 * (dMod + 5))
    Convert parsecs to Mpc: d / 10 ** 6

mpc_to_lightyears():
    https://www.astronomy.com/astronomy-for-beginners/why-is-a-parsec-3-26-light-years/
    https: //en.wikipedia.org/wiki/Parsec
    1 parsec = 3.26156 light-years. Since self.distance is Mpc, also multiply by 10^6.
"""

class Galaxy:
    def __init__(self, name):
        self.name = name # galaxy id
        self.data = [] # list of dictionaries containing keys mm (distance modulus, m-M), err (error on distance modulus), and mpc (distance in Megaparsecs)
        self.distance = None # distance in Mpc (Megaparsecs)

    def __lt__(self, other):
        return self.distance < other.distance

    def __repr__(self):
        return f"{self.name}({self.distance})"

    def add_data(self, mm, err, mpc):
        self.data.append({"mm": mm, "err": err, "mpc": mpc})

    def set_distance(self):
        # If there is only one galaxy in the database with the ID, set distance to the Mpc given in data
        if len(self.data) == 1:
            self.distance = self.data[0]["mpc"]

        else:
            # For multiple entries with the same ID, calculate a weighted mean of the distance modulus of each entry, then convert to Mpc
            numerator = []
            denominator = []

            for entry in self.data:
                # Calculate inverse square of error for weight and add to denominator list
                weight = 1 / (entry["err"] ** 2)
                denominator.append(weight)

                # Multiply distance modulus (m-M) and weight, then add to numerator list
                numerator.append(weight * entry["mm"])

            # Calculate weighted mean of distance modulus
            d_mod = sum(numerator) / sum(denominator)

            d_parsecs = 10 ** (0.2 * (d_mod + 5))
            d_mpc = d_parsecs / 10 ** 6

            self.distance = d_mpc

    def mpc_to_lightyears(self):
        return self.distance * 3.26156 * (10 ** 6)

    def get_distance(self):
        return self.distance

    def print_galaxy(self, num):
        print(f"{num}. {self.name} is {self.distance:0.5f} Megaparsecs away. That's {self.mpc_to_lightyears():0.5f} light-years!")
        print()
    
    def return_print_output(self):
        return f"{self.name} is {self.distance:0.5f} Megaparsecs away. That's {self.mpc_to_lightyears():0.5f} light-years!"
