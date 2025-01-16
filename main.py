import tkinter as tk
from tkinter import ttk, messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Moja Tkinter Aplikácia")
        self.root.geometry("800x600")
        self.root.configure(bg="#16315c")

        self.height_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.output_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Nadpis aplikácie
        title = ttk.Label(
            self.root,
            text="Fitness Kalkulačka",
            font=("Arial", 28, "bold"),
            background="#16315c",
            foreground="#d8dce3",
        )
        title.pack(pady=5)

        # Vstupy aplikácie
        hightLabel = ttk.Label(
            self.root,
            text="Zadajte svoju výšku v centimetroch",
            font=("Arial", 24, "bold"),
            background="#16315c",
            foreground="#d8dce3",
        )
        hightLabel.pack(pady=5)
        heightEntry = ttk.Entry(
            self.root,
            textvariable=self.height_var,
            font=("Arial", 16),
            width=50,
            justify="center",
        )
        heightEntry.pack(pady=(0, 20))

        weightLabel = ttk.Label(
            self.root,
            text="Zadajte svoju váhu v kilogramoch",
            font=("Arial", 24, "bold"),
            background="#16315c",
            foreground="#d8dce3",
        )
        weightLabel.pack(pady=5)
        weightEntry = ttk.Entry(
            self.root,
            textvariable=self.weight_var,
            font=("Arial", 16),
            width=50,
            justify="center",
        )
        weightEntry.pack(pady=(0, 20))

        ageLabel = ttk.Label(
            self.root,
            text="Zadajte svoj vek",
            font=("Arial", 24, "bold"),
            background="#16315c",
            foreground="#d8dce3",
        )
        ageLabel.pack(pady=5)
        ageEntry = ttk.Entry(
            self.root,
            textvariable=self.age_var,
            font=("Arial", 16),
            width=50,
            justify="center",
        )
        ageEntry.pack(pady=(0, 20))

        tlacidlo = ttk.Button(self.root, command=self.calculate_bmi, text="Vypočítať BMI")
        tlacidlo.pack(pady=20)

        vystup = ttk.Label(
            self.root,
            textvariable=self.output_var,
            font=("Arial", 16),
            background="#16315c",
            foreground="#d8dce3",
        )
        vystup.pack(pady=20)

    def calculate_bmi(self):
        try:
            height_cm = float(self.height_var.get().strip())
            weight = float(self.weight_var.get().strip())
            age = int(self.age_var.get().strip())

            if height_cm <= 0 or weight <= 0 or age <= 0:
                raise ValueError("Hodnoty musia byť kladné.")

            height_m = height_cm / 100  # Convert height to meters
            bmi = weight / (height_m ** 2)  # BMI calculation

            # Interpretácia výsledkov
            if bmi < 18.5:
                status = "Podváha"
            elif 18.5 <= bmi < 24.9:
                status = "Normálna hmotnosť"
            elif 25 <= bmi < 29.9:
                status = "Nadváha"
            else:
                status = "Obezita"

            self.output_var.set(f"Váš BMI: {bmi:.2f} ({status})")

        except ValueError as e:
            self.output_var.set("Chyba: Skontrolujte vstupy.")
            messagebox.showerror("Chyba", "Zadali ste nekorektné hodnoty. Uistite sa, že hodnoty sú kladné.")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
