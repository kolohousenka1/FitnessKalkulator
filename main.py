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

            # Interpretácia výsledkov s ohľadom na vek
            if age < 18:
                status = self.interpret_bmi_youth(bmi)
            elif age >= 65:
                status = self.interpret_bmi_elderly(bmi)
            else:
                status = self.interpret_bmi_adult(bmi)

            self.output_var.set(f"Váš BMI: {bmi:.2f} ({status})")

        except ValueError:
            self.output_var.set("Chyba: Skontrolujte vstupy.")
            messagebox.showerror("Chyba", "Zadali ste nekorektné hodnoty. Uistite sa, že hodnoty sú kladné.")

    def interpret_bmi_youth(self, bmi):
        if bmi < 18.5:
            return "Podváha (Konzultujte s lekárom)"
        elif 18.5 <= bmi < 24.9:
            return "Normálna hmotnosť"
        elif 25 <= bmi < 29.9:
            return "Nadváha (Konzultujte s lekárom)"
        else:
            return "Obezita (Konzultujte s lekárom)"

    def interpret_bmi_adult(self, bmi):
        if bmi < 18.5:
            return "Podváha"
        elif 18.5 <= bmi < 24.9:
            return "Normálna hmotnosť"
        elif 25 <= bmi < 29.9:
            return "Nadváha"
        else:
            return "Obezita"

    def interpret_bmi_elderly(self, bmi):
        if bmi < 22:
            return "Podváha (Konzultujte s lekárom)"
        elif 22 <= bmi < 27:
            return "Normálna hmotnosť"
        elif 27 <= bmi < 30:
            return "Mierna nadváha"
        else:
            return "Obezita (Konzultujte s lekárom)"


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
