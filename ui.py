import customtkinter as ctk

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("✴ Travel Destinations: Nearest Galaxies ✴")
        self.geometry("400x300")

        self.title("✴ Galaxy Traveler ✴")
        self.geometry("400x300")

        # Sidebar buttons
        ctk.CTkLabel(self, text="Options", font=("Helvetica", 18)).pack(pady=20)

        # ctk.CTkTextbox(self, )

        self.btn1 = ctk.CTkButton(self, text="Button 1", command=self.say_hi)
        self.btn1.pack(pady=10)

        self.btn2 = ctk.CTkButton(self, text="Button 2")
        self.btn2.pack(pady=10)

        # Main content area
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="left", fill="both", expand=True)

        self.label = ctk.CTkLabel(self.main_frame, text="Hello!", font=("Arial", 24))
        self.label.pack(pady=40)

    def say_hi(self):
        self.label.configure(text="Hi 👋")
