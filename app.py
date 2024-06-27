import customtkinter as ctk
from pages.main_page import MainPage
from pages.insulin_dosage_calculator import InsulinDosageCalculator
from pages.medicine_check import MedicineCheck

def show_frame(frame):
    for f in [main_page, insulin_dosage_calculator, medicine_check]:
        f.pack_forget()  # This will remove the frame from view
    frame.pack(fill='both', expand=True)

ctk.set_appearance_mode("Dark")  # Can be "System", "Dark", or "Light"
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title('Diabetes Management Application')
app.geometry('900x700')

# Create a frame for the navigation buttons
nav_frame = ctk.CTkFrame(app)
nav_frame.pack(side='left', fill='both', expand=False)

button_font = ctk.CTkFont("Roboto", 14, "bold")  # Define the font

# Navigation buttons
nav_button1 = ctk.CTkButton(nav_frame, text="A1C / eAG Calculator", font=button_font,
                            command=lambda: show_frame(main_page), fg_color="blue",
                            hover_color="darkblue", text_color="white",
                            border_width=2, border_color="lightblue", corner_radius=10)
nav_button1.pack(fill='both', expand=True, padx=10, pady=5)

nav_button2 = ctk.CTkButton(nav_frame, text="Insulin Dosage Calculator", font=button_font,
                            command=lambda: show_frame(insulin_dosage_calculator),
                            fg_color="red", hover_color="darkred", text_color="white",
                            border_width=2, border_color="pink", corner_radius=10)
nav_button2.pack(fill='both', expand=True, padx=10, pady=5)

nav_button3 = ctk.CTkButton(nav_frame, text="Medicine Check", font=button_font,
                            command=lambda: show_frame(medicine_check), fg_color="green",
                            hover_color="darkgreen", text_color="white",
                            border_width=2, border_color="lightgreen", corner_radius=10)
nav_button3.pack(fill='both', expand=True, padx=10, pady=5)

# Container for page content
content_frame = ctk.CTkFrame(app)
content_frame.pack(side='right', fill='both', expand=True)

# Initialize page frames
main_page = MainPage(content_frame)
insulin_dosage_calculator = InsulinDosageCalculator(content_frame)
medicine_check = MedicineCheck(content_frame)

# Initially show the main page
show_frame(main_page)

app.mainloop()