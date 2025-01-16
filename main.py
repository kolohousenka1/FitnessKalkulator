import tkinter as tk
from signal import valid_signals
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
        # Nadpis aplikácie.
        title = ttk.Label(self.root, text="Fitness Kalkulačka", font=("Arial", 28, "bold"), background="#16315c", foreground="#d8dce3")
        title.pack(pady=5)

        # Vstupy aplikácie.
        hightLabel = ttk.Label(self.root, text="Zadajte svoju vysku v centimetroch", font=("Arial", 24, "bold"), background="#16315c", foreground="#d8dce3")
        hightLabel.pack(pady=5)
        heightEntry = ttk.Entry(self.root, textvariable=self.height_var, font=("Arial", 16), width=50, justify="center")
        heightEntry.pack(pady=(0, 20))

        weightLabel = ttk.Label(self.root, text="Zadajte svoju vahu v kilogramoch", font=("Arial", 24, "bold"), background="#16315c", foreground="#d8dce3")
        weightLabel.pack(pady=5)
        weightLabel = ttk.Entry(self.root, textvariable=self.weight_var, font=("Arial", 16), width=50, justify="center")
        weightLabel.pack(pady=(0, 20))

        ageLabel = ttk.Label(self.root, text="Zadajte svoj vek", font=("Arial", 24, "bold"), background="#16315c", foreground="#d8dce3")
        ageLabel.pack(pady=5)
        ageEntry = ttk.Entry(self.root, textvariable=self.age_var, font=("Arial", 16), width=50, justify="center")
        ageEntry.pack(pady=(0, 20))

        tlacidlo = ttk.Button(self.root, command=self.urob, text="Stlač")
        tlacidlo.pack(pady=20)

        vystup = ttk.Label(self.root, textvariable=self.output_var, font=("Arial", 16))
        vystup.pack(pady=20)

    def urob(self):
        try:
            height = float(self.height_var.get().strip())
            weight = float(self.weight_var.get().strip())
            age = float(self.age_var.get().strip())

            self.output_var.set(f"Vek: {age}, vyska: {height}, vaha: {weight}")
        except ValueError:
            print("Boli zadane nekorektne hodnoty.")
            self.output_var.set("Nekorektne hodnoty.")


try:
    if __name__ == "__main__":
        root = tk.Tk()
        app = App(root)
        root.mainloop()
except Exception as e:
    print(f"An error occurred: {e}")
