import pandas as pd
import matplotlib.pyplot as plt

# 1 - importar os arquivos CSV e tratá-los conforme suas irregularidades. --> read para ler, encoding para transformar os bytes em caracteres 
# e o delimiter para indicar quais caracteres serão usados para a separação dos campos.

resultado = pd.read_csv(r'SP_turno_1.csv', encoding='latin-1', delimiter=';') 
eleitores = pd.read_csv(r'perfil_eleitorado_20200.csv', encoding='latin-1', delimiter=';')

primeira_linha_resultado = resultado.iloc[0] #---> teste para ver se está tudo correto no arquivo SP_turno_1
print(primeira_linha_resultado)

primeira_linha = eleitores.iloc[0]  #---> teste para ver a se está tudo correto no arquivo perfil_eleitorado_20200
print(primeira_linha)


############ FILTRAGEM DE DADOS ###############
# 2 - ver quais serão os campos úteis para consulta tabela eleitores: SG_UF, NM_MUNICIPIO, DS_GENERO, DS_FAIXA_ETARIA, DS_GRAU_ESCOLARIDADE
eleitores = eleitores[['SG_UF','NM_MUNICIPIO', 'DS_GENERO', 'DS_FAIXA_ETARIA', 'DS_GRAU_ESCOLARIDADE']]

#ver quais serão os campos úteis para consulta tabela resultado: SG_UF, NM_MUNICIPIO, DS_CARGO_PERGUNTA, SG_PARTIDO, QT_VOTOS, NM_VOTAVEL
resultado = resultado[['SG_UF', 'NM_MUNICIPIO', 'DS_CARGO_PERGUNTA', 'SG_PARTIDO', 'NM_VOTAVEL', 'QT_VOTOS']]

#filtrar para apenas eleitores e resultados de SAO PAULO
eleitores_sp = eleitores[eleitores['SG_UF'] == 'SP']

resultado_sp = resultado[resultado['SG_UF'] == 'SP']

# 3 - criando novas planilhas após a filtração de dados para as consultas e comandos rodarem mais rápido

eleitores_sp.to_csv('eleitores_sp.csv', sep=";", encoding='utf-8', index=False) 
resultado_sp.to_csv('resultado_sp.csv', sep=";", encoding='utf-8', index=False) 

# 4 - verificar se possui mais alguma inconsistência: estão corretos. todos os caracteres tratados igual ao print --- > tratados.png

# 5 - gerar uma consulta join que retorne informações IMPORTANTES a serem analisadas ->

resultado_sp_tratado = pd.read_csv(r'resultado_sp.csv', encoding='latin-1', delimiter=';')

eleitores_sp_tratado = pd.read_csv(r'eleitores_sp.csv', encoding='latin-1', delimiter=';')

# 6 - quantidade de votos para cada cargo 
total_votos_por_cargo = resultado_sp_tratado.groupby('DS_CARGO_PERGUNTA')['QT_VOTOS'].sum() # Agrupar por cargo e somar os votos
total_votos_por_cargo = total_votos_por_cargo.sort_values(ascending=False) # Ordenar os resultados por total de votos decrescente
print(total_votos_por_cargo)

# 7 - qual candidato foi mais votado em cada municipio
idx_max_votos_por_municipio = resultado_sp_tratado.groupby('NM_MUNICIPIO')['QT_VOTOS'].idxmax() # Encontrar o índice do candidato mais votado em cada município
candidato_mais_votado_por_municipio = resultado_sp_tratado.loc[idx_max_votos_por_municipio] # Selecionar as linhas correspondentes aos candidatos mais votados
print(candidato_mais_votado_por_municipio[['NM_MUNICIPIO', 'DS_CARGO_PERGUNTA', 'NM_VOTAVEL', 'QT_VOTOS']])

# 8 - qual foi o candidato mais votado para prefeito
candidatos_prefeito = resultado_sp_tratado[resultado_sp_tratado['DS_CARGO_PERGUNTA'] == 'Prefeito'] # Filtrar os candidatos a prefeito
candidato_mais_votado_prefeito = candidatos_prefeito.loc[candidatos_prefeito['QT_VOTOS'].idxmax()] # Encontrar o candidato mais votado para prefeito
print("Candidato mais votado para prefeito:")
print(candidato_mais_votado_prefeito[['NM_MUNICIPIO', 'DS_CARGO_PERGUNTA', 'NM_VOTAVEL', 'QT_VOTOS']])

# 9 - qual foi o candidato mais votado para vereador
candidatos_vereador = resultado_sp_tratado[resultado_sp_tratado['DS_CARGO_PERGUNTA'] == 'Vereador'] # Filtrar os candidatos a vereador
candidato_mais_votado_vereador = candidatos_vereador.loc[candidatos_vereador['QT_VOTOS'].idxmax()] # Encontrar o candidato mais votado para vereador
print("\nCandidato mais votado para vereador:")
print(candidato_mais_votado_vereador[['NM_MUNICIPIO', 'DS_CARGO_PERGUNTA', 'NM_VOTAVEL', 'QT_VOTOS']])

# 10 - qual o perfil do eleitorado (faixa etaria, genero, escolaridade, etc) media de cada estado
perfil_eleitorado_municipio = eleitores_sp_tratado.groupby('NM_MUNICIPIO').agg( # Calcular a média de gênero, faixa etária e escolaridade por município
    media_genero=('DS_GENERO', lambda x: x.mode()[0]),
    media_faixa_etaria=('DS_FAIXA_ETARIA', lambda x: x.mode()[0]),
    media_escolaridade=('DS_GRAU_ESCOLARIDADE', lambda x: x.mode()[0])
).reset_index()
print(perfil_eleitorado_municipio)

# 11 - bonus: grafico de pizza mostrando os 4 mais votados e quantos % representam os votos nulos 
candidatos_validos = resultado_sp_tratado[resultado_sp_tratado['NM_VOTAVEL'] != 'Branco'] # Filtrar o DataFrame para obter apenas os votos válidos (excluindo votos nulos)
votos_por_candidato = candidatos_validos.groupby('NM_VOTAVEL')['QT_VOTOS'].sum() # Calcular a soma de votos por candidato
votos_por_candidato = votos_por_candidato.sort_values(ascending=False) # Ordenar os candidatos pelo número de votos em ordem decrescente
top_5 = votos_por_candidato.head(5) # Pegar os 5 candidatos mais votados

# Criando o gráfico de pizza
plt.figure(figsize=(8, 8))
plt.pie(top_5, labels=top_5.index, autopct='%1.1f%%', startangle=140)
plt.title('Distribuição de Votos pelos 5 Candidatos Mais Votados (Excluindo Votos Nulos)')
plt.axis('equal')  # Mantém a proporção do gráfico de pizza
plt.show() #----> imagem graficopizza.png