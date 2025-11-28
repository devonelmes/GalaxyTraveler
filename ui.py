import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("✴ Travel Destinations: Nearest Galaxies ✴")
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
