import csv
import matplotlib.pyplot as plt

arquivo_csv = open('athlete_events.csv')
arquivo_processo = csv.reader(arquivo_csv)

dados = []
dados_limpos = []
verao = []
inverno = []
x = ["Inverno", "Verão"]

for i in arquivo_processo:
  dados.append(i)

for i in range(len(dados)):
  if (dados[i][13] == "Speed Skating Women's 500 metres" and dados[i][4] != 'NA' and dados[i][5] != 'NA' and dados[i][10] != 'NA'):
    dados_limpos.append(dados[i])

for i in range(len(dados_limpos)):
  altura = float(dados_limpos[i][4])
  peso = float(dados_limpos[i][5])
  imc = round(peso/((altura/100)*(altura/100)), 2)
  if (dados_limpos[i][10] == "Summer"):
    verao.append(imc)
  if (dados_limpos[i][10] == "Winter"):
    inverno.append(imc)
  
y = [inverno, verao]

def boxplotf():
 plt.boxplot(y, labels=x)
 plt.title("IMC | Todas as edições | Speed Skating Women's 500 metres")
 plt.xlabel('Tipo de olimpíada')
 plt.ylabel('IMC')
 plt.show()
 plt.savefig('boxplot.png')
 plt.close()