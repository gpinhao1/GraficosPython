import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FTIRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FTIR Plotter")

        self.load_button = tk.Button(root, text="Load Excel File", command=self.load_file)
        self.load_button.pack(pady=10)

        self.plot_button = tk.Button(root, text="Plot FTIR Spectrum", command=self.plot_spectrum)
        self.plot_button.pack(pady=10)

        self.figure = plt.Figure(figsize=(8, 5))
        self.canvas = FigureCanvasTkAgg(self.figure, master=root)
        self.canvas.get_tk_widget().pack()

        self.df = None

    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.df = pd.read_excel(file_path, header=1, decimal=',')
            print("File loaded successfully!")
            print(self.df.head())

    def plot_spectrum(self):
        if self.df is not None:
            ax = self.figure.add_subplot(111)
            ax.clear()
            ax.plot(self.df['cm-1'], self.df['%T'], color='black', linewidth=0.8)
            ax.invert_xaxis()
            ax.set_title('Espectro FTIR', fontsize=16)
            ax.set_xlabel(r'Número de Onda ($cm^{-1}$)', fontsize=12)
            ax.set_ylabel('Transmitância (%)', fontsize=12)
            ax.grid(True, linestyle='--', alpha=0.5)
            self.canvas.draw()
        else:
            print("Please load a file first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = FTIRApp(root)
    root.mainloop()
