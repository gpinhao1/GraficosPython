from tkinter import *
from tkinter import filedialog
import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
import os

class FTIRApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graficos FTIR")

        if os.path.exists("uerj.ico"):
            self.root.iconbitmap("uerj.ico")
        else:
            pass # Se não achar o ícone, abre sem ele (evita crash)

        self.frame = tk.Frame(root, width=280, height=200, bg="Black")
        self.frame.pack(pady=1, expand=True)

        self.status_label = tk.Label(self.frame, text="Bem vindo \n Escolha o Arquivo", font=("Times New Roman", 13))
        self.status_label.pack(pady=1, expand=True)

        self.load_button = tk.Button(root, text="Arquivo Excel", command=self.load_file,font=("Times New Roman", 13))
        self.load_button.pack(pady=1, expand=True)


        self.plot_button = tk.Button(root, text="Gere o Grafico", command=self.plot_spectrum,font=("Times New Roman", 13))
        self.plot_button.pack(pady=1, expand=True)

        self.df = None


    def load_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx;*.xls")])
        if file_path:
            self.df = pd.read_excel(file_path, header=1, decimal=',')
            print("File loaded successfully!")
            print(self.df.head())
            aviso = "Arquivo Carregado \n com Sucesso!"
            self.status_label.config(text=aviso)
        else:
            print("Erro ao carregar.")
            aviso = "Erro ao Carregar o Arquivo."
            self.status_label.config(text=aviso)

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

    def centralizar_janela(janela, largura, altura):

        # 1. Obter as dimensões da tela
        largura_tela = janela.winfo_screenwidth()
        altura_tela = janela.winfo_screenheight()

        # 2. Calcular a posição (x e y) para centralizar
        pos_x = int((largura_tela / 2) - (largura / 2))
        pos_y = int((altura_tela / 2) - (altura / 2))

        # 3. Aplicar a geometria com a posição calculada
        # Formato: "LarguraxAltura+PosicaoX+PosicaoY"
        janela.geometry(f'{largura}x{altura}+{pos_x}+{pos_y}')

if __name__ == "__main__":
    root = tk.Tk()
    largura = 250
    altura = 250
    FTIRApp.centralizar_janela(root, largura, altura)
    app = FTIRApp(root)
    root.mainloop()