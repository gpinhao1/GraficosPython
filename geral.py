import pandas as pd
import matplotlib.pyplot as plt

diretorio = r"/home/gp/Área de trabalho/FTIR/GraficosPython/FTIR/CA CSE BC .xlsx"


df = pd.read_excel(diretorio, header=1, decimal=',')

print(df.head())

# --- PLOTAGEM ---
plt.figure(figsize=(12, 6))


plt.plot(df['cm-1'], df['%T'], color='black', linewidth=0.8)

# Inverter eixo X (Padrão FTIR)
plt.gca().invert_xaxis()

# Formatação
plt.title('Espectro FTIR', fontsize=16)
plt.xlabel(r'Número de Onda ($cm^{-1}$)', fontsize=12)
plt.ylabel('Transmitância (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()