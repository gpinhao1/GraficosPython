import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

diretorio = r"C:\Users\Gabriel\PycharmProjects\Marcelo\FTIR\CA CSE BC .xlsx"
df = pd.read_excel(diretorio, engine='openpyxl')

print(df.head())

x = df.iloc[:, 0].values  # Pega todos os dados da coluna 0 (A)
y = df.iloc[:, 1].values  # Pega todos os dados da coluna 1 (B)

# 3. Configurar o Gráfico
plt.figure(figsize=(12, 6)) # Tamanho mais largo, padrão para espectros

# Plotar a linha (Geralmente preto ou azul escuro para FTIR)
plt.plot(df['cm-1'], df['%T'], color='black', linewidth=0.8)

# --- O TRUQUE DO FTIR ---
# Inverte o eixo X (de 4000 para 400)
plt.gca().invert_xaxis()

# 4. Formatação Técnica
plt.title('Espectro FTIR', fontsize=16)
# O uso de cifrões ($) permite escrever notação matemática (LaTeX) para o -1 sobrescrito
plt.xlabel(r'Número de Onda ($cm^{-1}$)', fontsize=12)
plt.ylabel('Transmitância (%)', fontsize=12)

# Grade para facilitar a leitura dos picos
plt.grid(True, which='major', linestyle='-', alpha=0.5)
plt.minorticks_on() # Adiciona marcações menores nos eixos
plt.grid(True, which='minor', linestyle=':', alpha=0.2)

# 5. Exibir
plt.tight_layout()
plt.show()


