"""
Resources:
    https://customtkinter.tomschimansky.com/
"""
import customtkinter
# import tkinter as tk
import customtkinter as ctk
from PIL import Image
from galaxy import Galaxy

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("✴ Travel Destinations: Nearest Galaxies ✴")
        self.geometry("1300x800")
        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure((0, 1), weight=1)
        #
        # # Partition window
        # self.menu_frame = customtkinter.CTkFrame(self)
        # self.menu_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsw")

        # self.bg_label = ctk.CTkLabel(self, image=self.bg_img, text="")
        # self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

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