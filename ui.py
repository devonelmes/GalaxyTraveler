"""References:
        https://customtkinter.tomschimansky.com/
"""
import time
from symbol import comparison

import customtkinter as ctk
from PIL import Image
from galaxy import Galaxy
from os.path import join
from helpers import heap_choose, quickselect, parse_galaxies

FONT = "Menlo"
NEON_PURPLE = "#9b4dff"


class MenuFrame(ctk.CTkFrame):
    # Create the menu frame in the top left of the window with title, welcome, prompt, k input field, and submit button.
    def __init__(self, master, size, image_path, width, height, on_submit=None):
        super().__init__(master, width=width, height=height, fg_color=NEON_PURPLE)
        self.size = size
        self.on_submit = on_submit
        self.selected_k = None

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
        self.title.pack(pady=(30, 10))

        # Welcome text
        welcome_text = "✴✴✴ Welcome, galaxy traveler! ✴✴✴"
        self.welcome = ctk.CTkLabel(self, text=welcome_text, fg_color="black", font=(FONT, 16))
        self.welcome.pack(pady=(10, 10))

        # Prompt text
        prompt_text = f"Please enter the number of closest galaxies\nto find between 1 and {self.size}:"
        self.prompt = ctk.CTkLabel(self, text=prompt_text, fg_color="black", font=(FONT, 14), justify="center")
        self.prompt.pack(pady=(10, 10))

        # Input box
        self.input = ctk.CTkEntry(self, width=120, font=(FONT, 14), fg_color="transparent", bg_color="transparent", justify="center")
        self.input.pack()

        # Submit button
        self.submit = ctk.CTkButton(self, width=120, fg_color=NEON_PURPLE, text="Submit", text_color="black", font=(FONT, 14), command=self.handle_submit)
        self.submit.pack(pady=(10, 5))

        # Error message (initially nothing)
        self.error = ctk.CTkLabel(self, text="", fg_color="black", font=(FONT, 14), text_color="red")
        self.error.pack(pady=(5, 0))

    def handle_submit(self):
        num = self.input.get()
        # Validate input
        try:
            k = int(num)
        except ValueError:
            self.error.configure(text="Invalid input. Please enter an integer.")
            return
        if not (1 <= k <= self.size):
            self.error.configure(text=f"Invalid input. Value must be between 1 and {self.size}")
            return

        # Valid input...
        self.error.configure(text="")
        self.selected_k = k

        if self.on_submit is not None:
            self.on_submit(k)


class DisplayFrame(ctk.CTkFrame):
    # Create galaxy display scrollable frame in bottom left of the window.
    def __init__(self, master, image_path, width, height):
        super().__init__(master, width=width, height=height, fg_color=NEON_PURPLE)

        # Make frame fixed size
        self.pack_propagate(False)

        # Place frame in bottom left of window
        self.place(x=0, y=300)

        # Set background to match window (from Lang's code in App())
        border = 12
        pil_image = Image.open(image_path)
        self.bg_img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(width-border, height-border))
        self.bg_label = ctk.CTkLabel(self, image=self.bg_img, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Set title
        self.title = ctk.CTkLabel(self, text="GALAXY DATA", fg_color="black", font=(FONT, 20, "bold"))
        self.title.pack(pady=(30, 10))

        # Create textbox for results
        self.textbox = ctk.CTkTextbox(self, width=400, height=350, fg_color="black", font=(FONT, 14), wrap="word")
        self.textbox.pack(pady=(10, 10))
        # Set textbox to "disabled" (not clickable, read-only)
        self.textbox.configure(state="disabled")


class GraphFrame(ctk.CTkFrame):
    # Create graph display canvas frame on the right side of the window.
    def __init__(self, master, image_path, width, height):
        super().__init__(master, width=width, height=height, fg_color=NEON_PURPLE)

        # Make frame fixed size
        self.pack_propagate(False)

        # Place frame in right side of window
        self.place(x=500, y=0)

        # Set background to match window (from Lang's code in App())
        border = 12
        pil_image = Image.open(image_path)
        self.bg_img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(width - border, height - border))
        self.bg_label = ctk.CTkLabel(self, image=self.bg_img, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Set title
        self.title = ctk.CTkLabel(self, text="GALAXY GRAPHIC", fg_color="black", font=(FONT, 20, "bold"))
        self.title.pack(pady=(30, 10))

        # Still obv need to implement canvas for graphics/animation
        # just putting this here for frame definition ?


class App(ctk.CTk):
    DIMENSIONS = (1300, 800)

    def __init__(self):
        super().__init__()

        self.galaxies = parse_galaxies("NED30.5.1-D-17.1.2-20200415.csv")

        # Set app window title and dimensions.
        self.title("✴ Travel Destinations: Nearest Galaxies ✴")
        self.geometry("1275x800")

        # Set background image.
        image_path = join("Starfield Images", "Starfield 8 - 1024x1024.png")
        pil_image = Image.open(image_path)
        self.bg_img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image,
                                   size=(self.DIMENSIONS[0], self.DIMENSIONS[1]))
        self.bg_label = ctk.CTkLabel(self, image=self.bg_img, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        self.output_label = ctk.CTkLabel(self, text=">")
        self.output_label.pack()

        # Set partition windows
        self.menu = MenuFrame(self, len(self.galaxies), image_path, width=500, height=300,
                              on_submit=self.display_closest)
        self.display = DisplayFrame(self, image_path, width=500, height=500)
        self.graphic = GraphFrame(self, image_path, width=775, height=800)

    def display_closest(self, k):
        k = self.menu.input.get()

        heap_start = time.time()
        heap_result = heap_choose(self.galaxies, int(k))
        heap_end = time.time()
        heap_time = heap_end - heap_start
        heap_string = (f"***********************************************\n"
                       f"Showing {k} closest galaxies using Heapsort...\n")
        for i, galaxy in enumerate(heap_result):
            line = f"{i + 1}. " + galaxy.return_print_output()
            heap_string += "\n" + line + "\n"
        heap_string += f"\n>>> Heapsort took {heap_time*1000:.4f} milliseconds."

        quick_start = time.time()
        quick_result = quickselect(self.galaxies, int(k))
        quick_end = time.time()
        quick_time = quick_end - quick_start
        quick_string = (f"\n\n***********************************************\n"
                        f"Showing {k} closest galaxies using Quickselect...\n")
        for i, galaxy in enumerate(quick_result):
            line = f"{i + 1}. " + galaxy.return_print_output()
            quick_string += "\n" + line + "\n"
        quick_string += f"\n>>> Quickselect took {quick_time*1000:.4f} milliseconds."

        comparison = "\n\n***********************************************\n"
        if quick_time > heap_time:
            # heap faster...
            speed = quick_time / heap_time
            comparison += f"\nHeapsort was {speed:.1f} times faster than Quickselect."
        elif heap_time > quick_time:
            # quickselect faster...
            speed = heap_time / quick_time
            comparison += f"\nQuickselect was {speed:.1f} times faster than Heapsort."
        else:
            comparison += f"\nHeapsort and Quickselect took the same amount of tine to execute."

        # Access display frame textbox, temporarily enable normal state, clear, fill, disable again
        textbox = self.display.textbox
        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        textbox.insert("end", heap_string)
        textbox.insert("end", quick_string)
        textbox.insert("end", comparison)
        textbox.configure(state="disabled")
