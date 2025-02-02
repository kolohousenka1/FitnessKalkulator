import tkinter as tk
from tkinter import ttk, messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Moja Tkinter Aplikácia")
        self.root.geometry("800x800")
        self.root.configure(bg="#16315c")

        self.height_var = tk.StringVar()
        self.weight_var = tk.StringVar()
        self.age_var = tk.StringVar()
        self.gender_var = tk.StringVar()
        self.output_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        # Nadpis aplikácie
        title = ttk.Label(
            self.root,
            text="Fitness Kalkulačka",
            font=("Arial", 24, "bold"),
            background="#16315c",
            foreground="#d8dce3",
        )
        title.pack(pady=5)

        # Vstupy aplikácie
        hightLabel = ttk.Label(
            self.root,
            text="Zadajte svoju výšku v centimetroch",
            font=("Arial", 20, "bold"),
            background="#16315c",
            foreground="#d8dce3",
        )
        hightLabel.pack(pady=5)
        heightEntry = ttk.Entry(
            self.root,
            textvariable=self.height_var,
            font=("Arial", 14),
            width=50,
            justify="center",
        )
        heightEntry.pack(pady=(0, 10))

        weightLabel = ttk.Label(
            self.root,
            text="Zadajte svoju váhu v kilogramoch",
            font=("Arial", 20, "bold"),
            background="#16315c",
            foreground="#d8dce3",
        )
        weightLabel.pack(pady=5)
        weightEntry = ttk.Entry(
            self.root,
            textvariable=self.weight_var,
            font=("Arial", 14),
            width=50,
            justify="center",
        )
        weightEntry.pack(pady=(0, 10))

        ageLabel = ttk.Label(
            self.root,
            text="Zadajte svoj vek",
            font=("Arial", 20, "bold"),
            background="#16315c",
            foreground="#d8dce3",
        )
        ageLabel.pack(pady=5)
        ageEntry = ttk.Entry(
            self.root,
            textvariable=self.age_var,
            font=("Arial", 14),
            width=50,
            justify="center",
        )
        ageEntry.pack(pady=(0, 10))

        self.gender_var.set("Male")

        tk.Radiobutton(
            root, text="Muž", variable=self.gender_var, value="Male", bg="#16315c", fg="#d8dce3"
        ).pack()
        tk.Radiobutton(
            root, text="Žena", variable=self.gender_var, value="Female", bg="#16315c", fg="#d8dce3"
        ).pack()

        tlacidlo = ttk.Button(self.root, command=self.run, text="Vypočítať BMI")
        tlacidlo.pack(pady=20)

        vystup = ttk.Label(
            self.root,
            textvariable=self.output_var,
            font=("Arial", 16),
            background="#16315c",
            foreground="#d8dce3",
        )
        vystup.pack(pady=20)

        # Canvas for Circular Graph
        self.canvas = tk.Canvas(self.root, width=400, height=400, bg="#16315c", highlightthickness=0)
        self.canvas.pack(pady=10)


    def run(self):
        categories_dict = {
            0: "Podváha (Konzultujte s lekárom)",
            1: "Normálna hmotnosť",
            2: "Nadváha (Konzultujte s lekárom)",
            3: "Obezita (Konzultujte s lekárom)"
        }
        calories_dict = {
            0: 1.3,
            1: 1,
            2: 0.9,
            3: 0.8
        }
        graph_text = "\nGráf percentá ľudí vo vašej vekovej skupine podľa percentá BMI: \npopis grafu: modrá = Podváha, zelená = Primeraná hmotnosť, oranžová = Mierna Obezita, červená = Ťažká Obezita"

        try:
            height_cm = float(self.height_var.get().strip())
            weight = float(self.weight_var.get().strip())
            age = int(self.age_var.get().strip())
            gender = self.gender_var.get().strip()

            if height_cm <= 0 or weight <= 0 or age <= 0:
                raise ValueError("Hodnoty musia byť kladné.")
            bmi = self.calculate_bmi(height_cm, weight)
            bmr = self.calculate_calories(height_cm, weight, age, gender)

            if age < 18:
                status = self.interpret_bmi_youth(bmi)
            elif age >= 65:
                status = self.interpret_bmi_elderly(bmi)
            else:
                status = self.interpret_bmi_adult(bmi)

            bmr_output = f"\nPotrebný počet kalórií na deň pre ľudí vo vašej kategórií: {calories_dict[status] * bmr}"
            self.output_var.set(f"Váš BMI: {bmi:.2f} ({categories_dict[status]})" + bmr_output + graph_text)
            self.update_graph(age)
        except ValueError:
            self.output_var.set("Chyba: Skontrolujte vstupy.")
            messagebox.showerror("Chyba", "Zadali ste nekorektné hodnoty. Uistite sa, že hodnoty sú kladné a je zadané pohlavie.")

    def calculate_bmi(self, height_cm, weight):
        height_m = height_cm / 100
        bmi = weight / (height_m ** 2)
        return bmi

    def interpret_bmi_youth(self, bmi):
        if bmi < 18.5:
            return 0
        elif 18.5 <= bmi < 24.9:
            return 1
        elif 25 <= bmi < 29.9:
            return 2
        else:
            return 3

    def interpret_bmi_adult(self, bmi):
        if bmi < 18.5:
            return 0
        elif 18.5 <= bmi < 24.9:
            return 1
        elif 25 <= bmi < 29.9:
            return 2
        else:
            return 3

    def interpret_bmi_elderly(self, bmi):
        if bmi < 22:
            return 0
        elif 22 <= bmi < 27:
            return 1
        elif 27 <= bmi < 30:
            return 2
        else:
            return 3

    def calculate_calories(self, height_cm, weight, age, gender):
        if gender == "Male":
            bmr = 10 * weight + 6.25 * height_cm - 5 * age + 5
        else:
            bmr = 10 * weight + 6.25 * height_cm - 5 * age - 161
        return bmr * 1.4

    def update_graph(self, age_category):
        self.canvas.delete("all")
        start_angle = 0

        if age_category <= 18:
            categories = [
                ("Podváha", 3, "#1f77b4"),
                ("Normálna hmotnosť", 63, "#2ca02c"),
                ("Nadváha", 21, "#ff7f0e"),
                ("Obezita", 13, "#d62728"),
            ]
        elif age_category < 65:
            categories = [
                ("Podváha", 2, "#1f77b4"),
                ("Normálna hmotnosť", 40, "#2ca02c"),
                ("Nadváha", 25, "#ff7f0e"),
                ("Obezita", 33, "#d62728"),
            ]

        elif age_category >= 65:
            categories = [
                ("Podváha", 3, "#1f77b4"),
                ("Normálna hmotnosť", 60, "#2ca02c"),
                ("Nadváha", 21, "#ff7f0e"),
                ("Obezita", 16, "#d62728"),
            ]

        for label, percentage, color in categories:
            extent = (360 * percentage) / 100
            self.canvas.create_arc(
                50, 50, 350, 350, start=start_angle, extent=extent, fill=color, outline=""
            )
            start_angle += extent


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
