"""References:
        https://customtkinter.tomschimansky.com/
"""
import customtkinter as ctk
from PIL import Image
from galaxy import Galaxy
from os.path import join
from helpers import HeapChoose, quickselect, parse_galaxies

FONT = "Menlo"


class MenuFrame(ctk.CTkFrame):
    # Create the menu frame in the top left of the window with title, welcome, prompt, k input field, and submit button.
    def __init__(self, master, size, image_path, width, height):
        super().__init__(master, width=width, height=height, fg_color="#9b4dff")
        self.size = size

        # Make frame fixed size
        self.pack_propagate(False)

        # Place frame in top left of window
        self.place(x=0, y=0)

        # Set background to match window (from Lang's code in App())
        border = 12
        pil_image = Image.open(image_path)
        self.bg_img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(width-border, height-border))
        self.bg_label = ctk.CTkLabel(self, image=self.bg_img, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Set title
        self.title = ctk.CTkLabel(self, text="MENU", fg_color="black", font=(FONT, 20, "bold"))
        self.title.pack(pady=(20, 10))

        # Welcome text
        welcome_text = "✴✴✴ Welcome, galaxy traveler! ✴✴✴"
        self.welcome = ctk.CTkLabel(self, text=welcome_text, fg_color="black", font=(FONT, 16))
        self.welcome.pack(pady=(10, 5))

        # Prompt text
        self.prompt = ctk.CTkLabel(self, text=f"Please enter the number of closest galaxies"
                                              f"\nto find between 1 and {self.size}:",
                                   fg_color="black", font=(FONT, 14), justify="center")
        self.prompt.pack(pady=(10, 10))

        # Input box
        self.input = ctk.CTkEntry(self, width=120, font=(FONT, 14), justify="center")
        self.input.pack()

        # Submit button


class DisplayFrame(ctk.CTkFrame):
    # Create galaxy display scrollable frame in bottom left of the window.
    DIMENSIONS = (500, 500)


class GraphFrame(ctk.CTkFrame):
    # Create graph display canvas frame on the right side of the window.
    DIMENSIONS = (800, 800)


class App(ctk.CTk):
    DIMENSIONS = (1300, 800)

    def __init__(self):
        super().__init__()

        self.galaxies = parse_galaxies("NED30.5.1-D-17.1.2-20200415.csv")

        # Set app window title and dimensions.
        self.title("✴ Travel Destinations: Nearest Galaxies ✴")
        self.geometry("1300x800")
        # self.grid_columnconfigure((0, 1), weight=1)
        # self.grid_rowconfigure(0, weight=1)
        # Set background image.
        image_path = join("Starfield Images", "Starfield 8 - 1024x1024.png")
        pil_image = Image.open(image_path)
        self.bg_img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(self.DIMENSIONS[0], self.DIMENSIONS[1]))
        self.bg_label = ctk.CTkLabel(self, image=self.bg_img, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Set partition windows
        self.menu = MenuFrame(self, size=len(self.galaxies), image_path=image_path, width=500, height=300)
        # Sidebar buttons
        # ctk.CTkLabel(self, text="Options", font=(FONT, 18)).pack(pady=20)
        #
        # self.k_entry = ctk.CTkEntry(self, width=120, placeholder_text="Enter k")
        # self.k_entry.pack(pady=8)
        #
        # self.lookup = ctk.CTkButton(self, text="Look up closest galaxies", command=self.display_closest)
        # self.lookup.pack(pady=10)

        # Main content area
        # self.main_frame = ctk.CTkFrame(self)
        # self.main_frame.pack(side="left", fill="none", expand=True)

        # self.label = ctk.CTkLabel(self.main_frame, text="Hello!", font=(FONT, 24))
        # self.label.pack(pady=40)

    def display_closest(self, *args):
        k = self.k_entry.get()
        if k.isdecimal():
            results = HeapChoose(self.galaxies, int(k))
            return results
        else:
            return []