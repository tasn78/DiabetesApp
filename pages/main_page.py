# pages/main_page.py
import os
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, Toplevel, Label
from PIL import Image, ImageTk

class MainPage(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, bg_color="#333333")  # Darker background for a modern look

        self.unit_var = tk.StringVar(value="mg/dL")
        self.conversion_var = tk.StringVar(value="A1C_to_eAG")

        self.title_label = ctk.CTkLabel(self, text="A1C / eAG Calculator", font=("Roboto", 28, "bold"), fg_color="#333333", bg_color="#DDDDDD", height=60)
        self.title_label.pack(pady=20, fill='x')

        self.radio_buttons_frame = ctk.CTkFrame(self)
        self.radio_buttons_frame.pack(pady=20, expand=True)

        self.conversion_type_label = ctk.CTkLabel(self.radio_buttons_frame, text="Choose conversion type:", font=("Roboto", 16), fg_color="#333333", bg_color="#DDDDDD")
        self.conversion_type_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))

        self.radio_a1c_to_eag = ctk.CTkRadioButton(self.radio_buttons_frame, text="A1C to eAG", variable=self.conversion_var, value="A1C_to_eAG", font=("Roboto", 14))
        self.radio_a1c_to_eag.grid(row=1, column=0, padx=10, sticky="e")
        
        self.radio_eag_to_a1c = ctk.CTkRadioButton(self.radio_buttons_frame, text="eAG to A1C", variable=self.conversion_var, value="eAG_to_A1C", font=("Roboto", 14))
        self.radio_eag_to_a1c.grid(row=1, column=1, padx=10, sticky="w")

        self.unit_type_label = ctk.CTkLabel(self.radio_buttons_frame, text="Choose units:", font=("Roboto", 16), fg_color="#333333", bg_color="#DDDDDD")
        self.unit_type_label.grid(row=2, column=0, columnspan=2, pady=(10, 0))

        self.radio_mg_dl = ctk.CTkRadioButton(self.radio_buttons_frame, text="mg/dL", variable=self.unit_var, value="mg/dL", font=("Roboto", 14))
        self.radio_mg_dl.grid(row=3, column=0, padx=10, sticky="e")

        self.radio_mmol_l = ctk.CTkRadioButton(self.radio_buttons_frame, text="mmol/L", variable=self.unit_var, value="mmol/L", font=("Roboto", 14))
        self.radio_mmol_l.grid(row=3, column=1, padx=10, sticky="w")

        self.entry_value = ctk.CTkEntry(self, font=("Roboto", 16), fg_color="#4E4E50", width=200, height=40)
        self.entry_value.pack(pady=20)

        self.calculate_button = ctk.CTkButton(self, text="Calculate", command=self.calculate, font=("Roboto", 16, "bold"), fg_color="#00897B", hover_color="#26A69A", width=200, height=40)
        self.calculate_button.pack(pady=20)

        self.label_result = ctk.CTkLabel(self, text="Result: ", font=("Roboto", 18, "bold"), fg_color="#333333", bg_color="#DDDDDD", height=40)
        self.label_result.pack(pady=20, fill='x')

        self.label_status = ctk.CTkLabel(self, text="", font=("Roboto", 14))
        self.label_status.pack(pady=10)

        self.help_button = ctk.CTkButton(self, text="Help Understanding Result", command=self.show_help, font=("Roboto", 16, "bold"), fg_color="darkred", hover_color="#26A69A", width=200, height=40)
        self.help_button.pack(side='right', padx=20, pady=20)

    def calculate(self):
        try:
            self.label_result.configure(text="")
            self.label_status.configure(text="", fg_color="#333333")
            source_value = float(self.entry_value.get())
            unit = self.unit_var.get()  # Get the currently selected unit

            if self.conversion_var.get() == "A1C_to_eAG":
                # Convert A1C to eAG, default is mg/dL
                result = 28.7 * source_value - 46.7
                result_type = "eAG"  # Set result type as eAG for further processing
                if unit == "mmol/L":
                    # Convert result to mmol/L if selected
                    result = result / 18.0182
                    display_unit = "mmol/L"
                else:
                    display_unit = "mg/dL"
            else:
                # Convert eAG to A1C, assumes input is in mg/dL
                result_type = "A1C"  # Set result type as A1C for further processing
                if unit == "mmol/L":
                    # If input is in mmol/L, convert it to mg/dL first for calculation
                    source_value = source_value * 18.0182
                result = (source_value + 46.7) / 28.7
                display_unit = "%"  # A1C is displayed as a percentage

            self.label_result.configure(text=f"Result: {result:.2f} {display_unit}")
            self.display_result(result, unit, result_type)  # Call display_result to show status based on ranges and type
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter a numeric value.")

    def display_result(self, result, unit, result_type):
        status_message, status_color = self.interpret_result(result, unit, result_type)
        self.label_status.configure(text=status_message, fg_color=status_color)
        self.label_status.pack(pady=10)
    
    def interpret_result(self, result, unit, result_type):
        unit_ranges = {
            "eAG": {
                "mg/dL": {
                    "Super Optimal": (67.1, 100.0),
                    "Optimal": (100.0, 128.3),
                    "Normal": (128.3, 139.9),
                    "Pre-Diabetes": (139.9, 153.6),
                    "Diabetes": (153.6, 185.9),
                    "Dangerous: Please contact a medical professional": (185.9, 214.9),
                    "Deathly: Please contact a medical professional immediately": (214.9, 244.0),
                    "Suicidal: Please contact a medical professional immediately": (244.0, 326.1)
                },
                "mmol/L": {
                    "Super Optimal": (3.7, 5.6),
                    "Optimal": (5.6, 7.1),
                    "Normal": (7.1, 7.8),
                    "Pre-Diabetes": (7.8, 8.5),
                    "Diabetes": (8.5, 10.3),
                    "Dangerous: Please contact a medical professional": (10.3, 11.9),
                    "Deathly: Please contact a medical professional immediately": (11.9, 13.5),
                    "Suicidal: Please contact a medical professional immediately": (13.5, 18.1)
                }
            },
            "A1C": {
                "Super Optimal": (4.0, 5.1),
                "Optimal": (5.1, 6.1),
                "Normal": (6.1, 6.5),
                "Pre-Diabetes": (6.5, 7.0),
                "Diabetes": (7.0, 8.0),
                "Dangerous: Please contact a medical professional": (8.0, 9.1),
                "Deathly: Please contact a medical professional immediately": (9.1, 10.1),
                "Suicidal: Please contact a medical professional immediately": (10.1, 13.0)
            }
        }
        
        # Select the correct range dictionary based on result_type and unit
        ranges = unit_ranges[result_type]
        if result_type == "eAG":
            ranges = ranges[unit]

        # Find the lowest and highest bounds across all categories
        lowest = min([r[0] for r in ranges.values()])
        highest = max([r[1] for r in ranges.values()])

        if result < lowest or result > highest:
            return "Dangerous level: Please contact a professional immediately", "#FF0000"

        status_color = "#FF0000"  # Default to red for undefined ranges
        for status, (low, high) in ranges.items():
            if low <= result <= high:
                if status in ["Super Optimal", "Optimal", "Normal"]:
                    status_color = "#008000"  # Green color for good range
                elif status in ["Pre-Diabetes", "Diabetes"]:
                    status_color = "#8B8000"  # Yellow color for caution
                elif status in ["Dangerous", "Deathly", "Suicidal"]:
                    status_color = "#FF0000"  # Red color for danger
                return f"Status: {status}", status_color

        return "Status: Result out of recognized range.", status_color
    
    # Shows table with all of the possible results
    def show_help(self):
        help_window = Toplevel(self)
        help_window.title("Help Information")

        script_dir = os.path.dirname(__file__)
        image_path = os.path.join(script_dir, '..', '..', 'shutterstock_1679494036.png')

        try:
            help_image = Image.open(image_path)
            base_width = 900
            w_percent = (base_width / float(help_image.size[0]))
            h_size = int((float(help_image.size[1]) * float(w_percent)))
            help_image = help_image.resize((base_width, h_size), Image.Resampling.LANCZOS)
            help_image_tk = ImageTk.PhotoImage(help_image)
            image_label = Label(help_window, image=help_image_tk)
            image_label.image = help_image_tk
            image_label.pack()
        except Exception as e:
            print(f"Error opening help image: {e}")
            messagebox.showerror("Error", "Cannot open help image.")