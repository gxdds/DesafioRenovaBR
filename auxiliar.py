import pandas as pd
import matplotlib.pyplot as plt

resultado_sp_tratado = pd.read_csv(r'resultado_sp.csv', encoding='latin-1', delimiter=';')
eleitores_sp_tratado = pd.read_csv(r'eleitores_sp.csv', encoding='utf-8', delimiter=';')


# Filtrar o DataFrame para obter apenas os votos válidos (excluindo votos nulos)
candidatos_validos = resultado_sp_tratado[resultado_sp_tratado['NM_VOTAVEL'] != 'Branco']

# Calcular a soma de votos por candidato
votos_por_candidato = candidatos_validos.groupby('NM_VOTAVEL')['QT_VOTOS'].sum()

# Ordenar os candidatos pelo número de votos em ordem decrescente
votos_por_candidato = votos_por_candidato.sort_values(ascending=False)

# Pegar os 5 candidatos mais votados
top_5 = votos_por_candidato.head(5)

# Criar o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(top_5, labels=top_5.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Votos pelos 5 Candidatos Mais Votados (Excluindo Votos Nulos)')
plt.axis('equal')  # Mantém a proporção do gráfico de pizza
plt.show()