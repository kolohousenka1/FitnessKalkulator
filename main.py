import tkinter as tk
from signal import valid_signals
from tkinter import ttk, messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Moja Tkinter Aplikácia")
        self.root.geometry("800x600")
        self.root.configure(bg="#16315c")

        self.vstup_var = tk.StringVar()
        self.vystup_var = tk.StringVar()


        self.create_widgets()

    def create_widgets(self):
        label = ttk.Label(self.root, text="Fitness Kalkulačka", font=("Arial", 24, "bold"), background="#16315c", foreground="#d8dce3")
        label.pack(pady=5)
        vstup = ttk.Entry(self.root, textvariable=self.vstup_var, font=("Arial", 16))
        vstup.pack(pady=20)
        tlacidlo = ttk.Button(self.root, command=self.urob, text="Stlač")
        tlacidlo.pack(pady=20)
        vystup = ttk.Label(self.root, textvariable=self.vystup_var, font=("Arial", 16))
        vystup.pack(pady=20)

    def urob(self):
        vstup_hodnota = self.vstup_var.get()
        if vstup_hodnota.strip():
            self.vystup_var.set(vstup_hodnota)
        else:
            self.vystup_var.set("Zadajte text.")







if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
