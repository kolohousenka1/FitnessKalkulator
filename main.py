import tkinter as tk
from tkinter import ttk, messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Moja Tkinter Aplikácia")
        self.root.geometry("800x600")  # Nastavenie veľkosti okna

        # Hlavný obsah
        self.create_widgets()

    def create_widgets(self):

        label = ttk.Label(self.root, text="tkinter zaklad", font=("Arial", 16))
        label.pack(pady=20)






if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
