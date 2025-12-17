from tkinter import *
from tkinter import filedialog
import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd

class FTIRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graficos FTIR")

        self.load_button = tk.Button(root, text="Arquivo Excel", command=self.load_file)
        self.load_button.pack(pady=10)

        self.plot_button = tk.Button(root, text="Gere o Grafico", command=self.plot_spectrum)
        self.plot_button.pack(pady=10)

        self.df = None

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.df = pd.read_excel(file_path, header=1, decimal=',')
            print("File loaded successfully!")
            print(self.df.head())
        else:
            print("Erro ao carregar.")

    def plot_spectrum(self):
        if self.df is not None:
            plt.figure(figsize=(12, 6))
            plt.plot(self.df['cm-1'], self.df['%T'], color='black', linewidth=0.8)
            plt.gca().invert_xaxis()
            plt.title('Espectro FTIR', fontsize=16)
            plt.xlabel(r'Número de Onda ($cm^{-1}$)', fontsize=12)
            plt.ylabel('Transmitância (%)', fontsize=12)
            plt.grid(True, linestyle='--', alpha=0.5)
            plt.tight_layout()
            plt.show()
        else:
            print("Carregue o Arquivo Primeiro.")

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("300x300")
    app = FTIRApp(root)
    root.mainloop()