"""References:
        https://customtkinter.tomschimansky.com/
"""
import customtkinter as ctk
from PIL import Image
from galaxy import Galaxy
from os.path import join



class App(ctk.CTk):
    DIMENSIONS = (1300, 800)

    def __init__(self):
        super().__init__()
        # Set app window title and dimensions.
        self.title("✴ Travel Destinations: Nearest Galaxies ✴")
        self.geometry("1300x800")
        # Set background image.
        image_path = join("Starfield Images", "Starfield 8 - 1024x1024.png")
        pil_image = Image.open(image_path)
        self.bg_img = ctk.CTkImage(light_image=pil_image, dark_image=pil_image, size=(self.DIMENSIONS[0], self.DIMENSIONS[1]))
        self.bg_label = ctk.CTkLabel(self, image=self.bg_img, text="")
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Partition window (Menu - top right, 500x300; Scroll galaxy display - bottom left, 500x500; graph - right, 800x800)
        # code
        # Sidebar buttons
        ctk.CTkLabel(self, text="Options", font=("Helvetica", 18)).pack(pady=20)

        self.k_entry = ctk.CTkEntry(self, width=120, placeholder_text="Enter k")
        self.k_entry.pack(pady=8)
        self.k_entry.bind("<KeyRelease>", self.on_k_change)

        self.lookup = ctk.CTkButton(self, text="Look up closest galaxies")
        self.lookup.pack(pady=10)

        # Main content area
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="left", fill="none", expand=True)

        self.label = ctk.CTkLabel(self.main_frame, text="Hello!", font=("Arial", 24))
        self.label.pack(pady=40)

    def on_k_change(self):
        pass