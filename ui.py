import customtkinter as ctk
from galaxy import Galaxy

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("✴ Travel Destinations: Nearest Galaxies ✴")
        self.geometry("1000x600")

        # Sidebar buttons
        ctk.CTkLabel(self, text="Options", font=("Helvetica", 18)).pack(pady=20)

        self.k_entry = ctk.CTkEntry(self, width=120, placeholder_text="Enter k")
        self.k_entry.pack(pady=8)
        self.k_entry.bind("<KeyRelease>", self.on_k_change)

        self.lookup = ctk.CTkButton(self, text="Look up closest galaxies")
        self.lookup.pack(pady=10)

        # Main content area
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="left", fill="both", expand=True)

        self.label = ctk.CTkLabel(self.main_frame, text="Hello!", font=("Arial", 24))
        self.label.pack(pady=40)

    def on_k_change():
        pass