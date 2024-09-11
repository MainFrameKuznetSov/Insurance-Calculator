import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk

class InsuranceCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Insurance Premium Calculator")
        master.geometry("600x450")
        master.resizable(True,True)
        master.configure(bg="#e3f2fd")

        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12), padding=10, background="#e3f2fd")
        style.configure("TButton", font=("Arial", 12), padding=8, relief="flat")
        style.configure("TEntry", font=("Arial", 12), padding=5)
        style.configure("TCombobox", font=("Arial", 12), padding=5)

        self.frame_main = ttk.Frame(master, padding=10)
        self.frame_main.pack(fill="both", expand=True)

        self.canvas = tk.Canvas(self.frame_main, bg="#e3f2fd")
        self.canvas.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.frame_main, orient="vertical", command=self.canvas.yview)
        self.scrollbar.pack(side="right", fill="y")

        self.frame_inner = ttk.Frame(self.canvas, padding=10, width=580, height=600)
        self.canvas.create_window((0, 0), window=self.frame_inner, anchor="nw")
        self.frame_inner.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))

        self.logo = Image.open("logo.png") 
        self.logo = self.logo.resize((100, 100))
        self.logo_photo = ImageTk.PhotoImage(self.logo)
        self.label_logo = tk.Label(self.frame_main, image=self.logo_photo, bg="#e3f2fd")
        self.label_logo.place(x=550, y=10, anchor="ne")

        self.create_widgets()

        self.master.bind_all("<MouseWheel>", self.on_mouse_wheel)

    def on_resize(self, event):
    # Get the new window width and height
        width = self.master.winfo_width()
        height = self.master.winfo_height()

    # Adjust the width and height of the inner frame to match the new window size
        self.frame_inner.config(width=width - 20, height=height - 20)

    # Optionally, adjust logo position if needed
        self.label_logo.place(x=width - 110, y=10, anchor="ne")
    
    # Adjust any other widgets if needed


    def create_widgets(self):
        self.label_title = ttk.Label(self.frame_inner, text="Insurance Premium Calculator", font=("Arial", 18, "bold"), background="#0288d1", foreground="white")
        self.label_title.grid(row=0, column=0, columnspan=2, pady=15, sticky="EW")

        self.label_age = ttk.Label(self.frame_inner, text="Age:", background="#e3f2fd")
        self.label_age.grid(row=1, column=0, sticky="E", padx=10)
        self.entry_age = ttk.Entry(self.frame_inner)
        self.entry_age.grid(row=1, column=1, padx=10, pady=5, sticky="EW")

        self.label_gender = ttk.Label(self.frame_inner, text="Gender:", background="#e3f2fd")
        self.label_gender.grid(row=2, column=0, sticky="E", padx=10)
        self.gender_var = tk.StringVar()
        self.gender_var.set("Male")
        self.dropdown_gender = ttk.Combobox(self.frame_inner, textvariable=self.gender_var, values=["Male", "Female"])
        self.dropdown_gender.grid(row=2, column=1, padx=10, pady=5, sticky="EW")

        self.label_coverage = ttk.Label(self.frame_inner, text="Coverage Type:", background="#e3f2fd")
        self.label_coverage.grid(row=3, column=0, sticky="E", padx=10)
        self.coverage_var = tk.StringVar()
        self.coverage_var.set("Basic")
        self.dropdown_coverage = ttk.Combobox(self.frame_inner, textvariable=self.coverage_var, values=["Basic", "Standard", "Premium"])
        self.dropdown_coverage.grid(row=3, column=1, padx=10, pady=5, sticky="EW")

        self.label_occupation = ttk.Label(self.frame_inner, text="Occupation:", background="#e3f2fd")
        self.label_occupation.grid(row=4, column=0, sticky="E", padx=10)
        self.occupation_var = tk.StringVar()
        self.occupation_var.set("Service")
        self.dropdown_occupation = ttk.Combobox(self.frame_inner, textvariable=self.occupation_var, values=["Service", "Business", "Self-employed"])
        self.dropdown_occupation.grid(row=4, column=1, padx=10, pady=5, sticky="EW")

        self.label_marital_status = ttk.Label(self.frame_inner, text="Marital Status:", background="#e3f2fd")
        self.label_marital_status.grid(row=5, column=0, sticky="E", padx=10)
        self.marital_var = tk.StringVar()
        self.marital_var.set("Single")
        self.dropdown_marital_status = ttk.Combobox(self.frame_inner, textvariable=self.marital_var, values=["Single", "Married", "Divorced"])
        self.dropdown_marital_status.grid(row=5, column=1, padx=10, pady=5, sticky="EW")

        self.label_health_conditions = ttk.Label(self.frame_inner, text="Health Conditions:", background="#e3f2fd")
        self.label_health_conditions.grid(row=6, column=0, sticky="E", padx=10)
        self.health_var = tk.StringVar()
        self.health_var.set("Perfect")
        self.dropdown_health_conditions = ttk.Combobox(self.frame_inner, textvariable=self.health_var, values=["Perfect", "Handicapped", "Diseased"])
        self.dropdown_health_conditions.grid(row=6, column=1, padx=10, pady=5, sticky="EW")

        self.calculate_button = ttk.Button(self.frame_inner, text="Calculate Premium", command=self.calculate_premium)
        self.calculate_button.grid(row=7, column=0, columnspan=2, pady=20, sticky="EW")
        self.calculate_button.configure(style="TButton")

        self.label_result = ttk.Label(self.frame_inner, text="", font=("Arial", 14, "italic"), background="#e3f2fd", foreground="#0288d1")
        self.label_result.grid(row=8, column=0, columnspan=2, pady=15, sticky="EW")
        self.label_result.configure(anchor="center")

        self.label_custom_rates = ttk.Label(self.frame_inner, text="Custom Rates (in ₹):", font=("Arial", 14, "bold"), background="#0288d1", foreground="white")
        self.label_custom_rates.grid(row=9, column=0, columnspan=2, pady=10, sticky="EW")

        self.age_rate_entries = {}
        self.create_rate_entry(self.frame_inner, "Age < 18:", 10)
        self.create_rate_entry(self.frame_inner, "Age 18-25:", 11)
        self.create_rate_entry(self.frame_inner, "Age 26-40:", 12)
        self.create_rate_entry(self.frame_inner, "Age 41-60:", 13)
        self.create_rate_entry(self.frame_inner, "Age > 60:", 14)

        self.label_custom_coverage = ttk.Label(self.frame_inner, text="Coverage Rate Multiplier:", background="#e3f2fd")
        self.label_custom_coverage.grid(row=15, column=0, sticky="E", padx=10)
        self.entry_custom_coverage = ttk.Entry(self.frame_inner)
        self.entry_custom_coverage.grid(row=15, column=1, padx=10, pady=5, sticky="EW")

        self.frame_inner.grid_columnconfigure(0, weight=1)
        self.frame_inner.grid_columnconfigure(1, weight=1)

    def create_rate_entry(self, frame, label_text, row):
        label = ttk.Label(frame, text=label_text, background="#e3f2fd")
        label.grid(row=row, column=0, sticky="E", padx=10)
        entry = ttk.Entry(frame)
        entry.grid(row=row, column=1, padx=10, pady=5, sticky="EW")
        self.age_rate_entries[label_text] = entry

    def calculate_premium(self):
        basic_multiplier = 1.0
        standard_multiplier = 1.5
        premium_multiplier = 2.0
    
        try:
            age = int(self.entry_age.get())
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid age.")
            return
    
        gender = self.gender_var.get()
        coverage = self.coverage_var.get()
        occupation = self.occupation_var.get()
        marital_status = self.marital_var.get()
        health_conditions = self.health_var.get()
    
        try:
            rate_under_18 = float(self.age_rate_entries["Age < 18:"].get() or 0)
            rate_18_25 = float(self.age_rate_entries["Age 18-25:"].get() or 0)
            rate_26_40 = float(self.age_rate_entries["Age 26-40:"].get() or 0)
            rate_41_60 = float(self.age_rate_entries["Age 41-60:"].get() or 0)
            rate_above_60 = float(self.age_rate_entries["Age > 60:"].get() or 0)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid custom rates.")
            return
    
        coverage_multiplier = 1
        try:
            coverage_multiplier = float(self.entry_custom_coverage.get() or 1)
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid coverage rate multiplier.")
            return
    
        base_premium = 0
        if age < 18:
            base_premium = rate_under_18
        elif age <= 25:
            base_premium = rate_18_25
        elif age <= 40:
            base_premium = rate_26_40
        elif age <= 60:
            base_premium = rate_41_60
        else:
            base_premium = rate_above_60
    
        if coverage == "Basic":
            base_premium *= basic_multiplier
        elif coverage == "Standard":
            base_premium *= standard_multiplier
        elif coverage == "Premium":
            base_premium *= premium_multiplier
    
        base_premium *= coverage_multiplier
    
        if gender == "Female":
            base_premium *= 1.05
    
        if marital_status == "Married":
            base_premium *= 0.95
        elif marital_status == "Divorced":
            base_premium *= 1.1
    
        if health_conditions == "Handicapped":
            base_premium *= 1.25
        elif health_conditions == "Diseased":
            base_premium *= 1.5
    
        self.label_result.configure(text=f"Your calculated premium is: ₹{base_premium:.2f}")


    def on_mouse_wheel(self, event):
        self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")

if __name__ == "__main__":
    root = tk.Tk()
    app = InsuranceCalculator(root)
    root.mainloop()
