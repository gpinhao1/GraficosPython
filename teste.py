import pandas as pd
import matplotlib.pyplot as plt

import pandas as pd
import matplotlib.pyplot as plt

diretorio = input("Caminho:")


# --- AQUI ESTÁ A MÁGICA ---
# header=1: Pega a linha 2 do Excel como título (ignora a linha "Criado com...")
# decimal=',': Converte "99,93" para o número 99.93 corretamente
df = pd.read_excel(diretorio, header=1, decimal=',')

# Verifica se leu certo (opcional, mas bom pra garantir)
print(df.head())

# --- PLOTAGEM ---
plt.figure(figsize=(12, 6))

# Como definimos header=1, agora podemos chamar as colunas pelos nomes que aparecem na imagem
# Nota: O nome da coluna no Excel é 'cm-1', mas verifique se não tem espaços extras
# Se der erro de nome, troque df['cm-1'] por df.iloc[:, 0]
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