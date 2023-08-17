# DesafioRenovaBR
 
O primeiro passo foi criar um ambiente virtual e instalar as bibliotecas que seriam utilizadas (pandas para lidar com as tabelas e matplotlib para criar o gráfico de pizza)
no arquivo main, cada passo está enumerado:

Passo 1: Foram importados os arquivos .csv para ler usando os tratamentos conforme os comentários no próprio código.
após importar, foi testado um print da primeira linha para ver se importou corretamente e já identificar algumas inconsistências. (printado apenas uma linha da tabela para carregar mais rápido).

Passo 2: Filtragem de dados, é onde começo a pegar apenas os campos úteis para o que iríamos fazer, conforme nos comentários no próprio código.
após fazer a filtragem dos campos que queria, fiz a filtragem para apenas São Paulo, conforme a proposta do desafio.

Passo 3: Criar novas planilhas baseadas nos novos filtros para minimizar o espaço ocupado pelas antigas com muitas linhas e bem pesada.

Passo 4: Verificar se havia sobrado algum caractere especial não tratado. Conforme a imagem neste repositório nomeada "tratados.png".

Passo 5: Importando e lendo os arquivos novos (filtrados e menores em tamanho) para realizar CONSULTAS.

Passo 6: Quantidade de votos por cargo.
neste passo, foi usado o método groupby para agrupar os cargos que apareciam varias vezes e a quantidade de votos com o comando ".sum()" para somá-los.

Passo 7: Qual candidato foi mais votado em cada municipio.
neste passo, foi utilizado o método groupby novamente para agrupar o nome dos municipios e a quantidade de votos com o comando ".idmax()" para encontrar o mais votado e após isso printar as linhas correspondentes aos mais votados.

Passo 8: Qual o candidato com mais votos para prefeito.
neste passo, foi filtrado apenas os votos para prefeito, o comando ".idmax()" para encontrar a linha em "QT_VOTOS" que possui mais votos, printando o nome do municipio, o cargo, o nome e a quantidade de votos

Passo 9: Qual o candidato com mais votos para vereador.
neste passo foram usados os mesmos comandos do anterior, porém o filtro foi "Vereador" na coluna 'DS_CARGO_PERGUNTA' que era a correspondente ao cargo.

Passo 10: Qual a média de faixa etária, escolaridade e gênero (quais mais aparecem) em cada município.
neste passo, o lambda foi usado para criar como se fosse uma "mini-funçao", o ".mode()", pega o valor mais frequente para aquele grupo de município.

Passo 11: Gráfico de pizza mostrando os 4 mais votados e quantos % representam os votos nulos.
neste passo, utilizamos a biblioteca matplotlib para: 1°, definir o tamanho da imagem, 2° setar a posiçao e quais serão os elementos do gráfico de pizza, 3° título da figura, 4° manter a proporção e 5° por último mostrar o gráfico no comando ".show()"

O arquivo "auxiliar.py" foi usado para fazer os testes dos comandos utilizados para que não fosse necessário ficar comentando as linhas de código, evitando a perda de tempo e mantendo a organização do código
