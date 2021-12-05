import matplotlib.pyplot as plt
import csv
import statistics

arquivo_csv = open('athlete_events.csv')
arquivo_processo = csv.reader(arquivo_csv)

dados = []
dados_limpos = []
imc_masculino_2016 = []
imc_masculino_2014 = []
imc_masculino_2012 = []
imc_masculino_2010 = []
imc_masculino_2008 = []
imc_feminino_2016 = []
imc_feminino_2014 = []
imc_feminino_2012 = []
imc_feminino_2010 = []
imc_feminino_2008 = []

for i in arquivo_processo:
  dados.append(i)

for i in range(len(dados)):
  if (dados[i][14] != 'NA' and dados[i][4] != 'NA' and dados[i][4] != 'Height' and dados[i][5] != 'NA' and dados[i][10] == 'Winter'):
    dados_limpos.append(dados[i])



for i in range(len(dados_limpos)):
  altura = float(dados_limpos[i][4])
  peso = float(dados_limpos[i][5])
  imc = round(peso/((altura/100)*(altura/100)), 2)
  if (dados_limpos[i][2] == "M" and dados_limpos[i][9] == "2016"):
    imc_masculino_2016.append(imc)
  if (dados_limpos[i][2] == "M" and dados_limpos[i][9] == "2014"):
    imc_masculino_2014.append(imc)
  if (dados_limpos[i][2] == "M" and dados_limpos[i][9] == "2012"):
    imc_masculino_2012.append(imc)
  if (dados_limpos[i][2] == "M" and dados_limpos[i][9] == "2010"):
    imc_masculino_2010.append(imc)
  if (dados_limpos[i][2] == "M" and dados_limpos[i][9] == "2008"):
    imc_masculino_2008.append(imc)
  if (dados_limpos[i][2] == "F" and dados_limpos[i][9] == "2016"):
    imc_feminino_2016.append(imc)
  if (dados_limpos[i][2] == "F" and dados_limpos[i][9] == "2014"):
    imc_feminino_2014.append(imc)
  if (dados_limpos[i][2] == "F" and dados_limpos[i][9] == "2012"):
    imc_feminino_2012.append(imc)
  if (dados_limpos[i][2] == "F" and dados_limpos[i][9] == "2010"):
    imc_feminino_2010.append(imc)
  if (dados_limpos[i][2] == "F" and dados_limpos[i][9] == "2008"):
    imc_feminino_2008.append(imc)


def linhasf():
  x = [2016, 2014, 2012, 2010, 2008]
  yM = [statistics.mean(imc_masculino_2016 or [0]), statistics.mean(imc_masculino_2014 or [0]), statistics.mean(imc_masculino_2012 or [0]), statistics.mean(imc_masculino_2010 or [0]), statistics.mean(imc_masculino_2008 or [0])]
  yF = [statistics.mean(imc_feminino_2016 or [0]), statistics.mean(imc_feminino_2014 or [0]), statistics.mean(imc_feminino_2012 or [0]), statistics.mean(imc_feminino_2010 or [0]), statistics.mean(imc_feminino_2008 or [0])] 
  plt.plot(x, yM)
  plt.plot(x, yF)
  plt.title('Média IMC | 5 últimas edições de inverno | Medalhistas')
  plt.xlabel('Anos (edições)')
  plt.ylabel('Média IMC')
  plt.savefig('linha.png')
  plt.show()
  plt.close()