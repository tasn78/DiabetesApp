# pages/medicine_check.py
import customtkinter as ctk
import tkinter as tk

class MedicineCheck(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent, bg_color="#333333")
        self.configure(bg_color="#2a2d2e")

        # Title label
        label = ctk.CTkLabel(self, text="Medicine Check", font=("Roboto", 28, "bold"), fg_color="#333333", bg_color="#DDDDDD", height=60)
        label.pack(pady=20, fill='x')

        # Entry for medication name input
        self.search_entry = ctk.CTkEntry(self, placeholder_text="Enter a medication name", width=400, height=40)
        self.search_entry.pack(pady=10)

        # Button to trigger the search
        self.search_button = ctk.CTkButton(self, text="Search", command=self.search_medication, fg_color="#00897B", hover_color="#26A69A", width=200, height=40)
        self.search_button.pack(pady=5)

        # Dictionary of medications and their effects
        self.medication_effects = {
            "Insulin": "Regulates blood sugar levels.",
            "Glipizide": "Lowers blood sugar levels by stimulating the pancreas to release more insulin.",
            "Metformin": "Lowers blood sugar levels by reducing glucose production in the liver and improving insulin sensitivity.",
            "Prednisone": "Used to treat inflammation and immune system disorders.",
            "Propranolol": "Used to treat high blood pressure, irregular heart rhythms, and other heart conditions.",
            "Clozapine": "Used to treat schizophrenia.",
            "Canagliflozin": "Lowers blood sugar levels by causing the kidneys to remove sugar from the body through urine."
        }

        # Result label with word wrap
        self.result_label = ctk.CTkLabel(self, text="", font=("Roboto", 16, "bold"),
                                         fg_color="#333333", bg_color="#DDDDDD",
                                         wraplength=350, height=100, width=400)  # Adjusted for bigger size and wrapping
        self.result_label.pack(pady=20, fill='x')

        # Button to reveal and hide medication list
        self.toggle_list_button = ctk.CTkButton(self, text="Toggle Medication List", command=self.toggle_medication_list, fg_color="darkblue", hover_color="blue", width=200, height=40)
        self.toggle_list_button.pack(pady=5)

        # Medication list initially hidden
        self.medication_list_frame = ctk.CTkFrame(self)
        self.medication_list_frame.pack_forget()
        
        for medication in sorted(self.medication_effects.keys()):
            med_label = ctk.CTkLabel(self.medication_list_frame, text=medication, font=("Roboto", 14))
            med_label.pack(pady=2)

    def toggle_medication_list(self):
        if self.medication_list_frame.winfo_ismapped():
            self.medication_list_frame.pack_forget()
        else:
            self.medication_list_frame.pack(pady=10)

    def search_medication(self):
        search_term = self.search_entry.get().strip().lower()
        found = False
        for medication, effect in self.medication_effects.items():
            if search_term == medication.lower():
                self.result_label.configure(text=f"{medication}: {effect}")
                found = True
                break
        if not found:
            self.result_label.configure(text=f"No results found for '{search_term}'.")