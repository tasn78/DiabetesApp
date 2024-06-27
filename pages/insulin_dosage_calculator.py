# pages/insulin_dosage_calculator.py
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

class InsulinDosageCalculator(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, bg_color="#333333")

        # Title
        self.title_label = ctk.CTkLabel(self, text="Simplified Insulin Dosage Calculator",
                                        font=("Roboto", 28, "bold"), fg_color="#333333",
                                        bg_color="#DDDDDD", height=60)
        self.title_label.pack(pady=20, fill='x')

        # Input for weight
        self.weight_entry = ctk.CTkEntry(self, font=("Roboto", 16), width=200, height=40)
        self.weight_entry.pack(pady=10)

        # Radio buttons for lbs and kg
        self.radio_frame = ctk.CTkFrame(self)
        self.radio_frame.pack(pady=10)
        
        self.weight_unit_var = tk.StringVar(value="Pounds")
        self.radio_pounds = ctk.CTkRadioButton(self.radio_frame, text="Pounds", variable=self.weight_unit_var, value="Pounds",
                                               font=("Roboto", 14))
        self.radio_pounds.pack(side="left", padx=50)  # Added padding for centering

        self.radio_kilograms = ctk.CTkRadioButton(self.radio_frame, text="Kilograms", variable=self.weight_unit_var, value="Kilograms",
                                                 font=("Roboto", 14))
        self.radio_kilograms.pack(side="right", padx=50)  # Added padding for centering

        # Calculate Button
        self.calculate_button = ctk.CTkButton(self, text="Calculate Dosage", command=self.calculate_insulin_dose,
                                              font=("Roboto", 16, "bold"), fg_color="#00897B", hover_color="#26A69A",
                                              width=200, height=40)
        self.calculate_button.pack(pady=20)

        # Label for Results
        self.result_label = ctk.CTkLabel(self, text="", font=("Roboto", 16, "bold"),
                                         fg_color="#333333", bg_color="#DDDDDD",
                                         height=100, width=400)  # Adjusted for bigger size
        self.result_label.pack(pady=20, fill='x')

    def calculate_insulin_dose(self):
        try:
            weight = float(self.weight_entry.get())
            weight_unit = self.weight_unit_var.get()

            # Calculate total daily insulin requirement
            if weight_unit == "Pounds":
                total_daily_insulin = weight / 4
            else:  # Kilograms
                total_daily_insulin = weight * 0.55

            # Calculate basal and bolus doses
            basal_insulin = total_daily_insulin * 0.4
            bolus_insulin = total_daily_insulin * 0.6
            bolus_per_meal = bolus_insulin / 3  # Assuming 3 meals per day

            # Display results
            result_text = (f"Total Daily Insulin: {total_daily_insulin:.1f} units\n"
                           f"Basal Insulin: {basal_insulin:.1f} units\n"
                           f"Bolus Insulin: {bolus_insulin:.1f} units total\n"
                           f"Bolus per Meal: {bolus_per_meal:.1f} units (assuming 3 meals a day)")
            self.result_label.configure(text=result_text)
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid weight.")