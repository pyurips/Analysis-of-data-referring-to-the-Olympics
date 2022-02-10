import matplotlib.pyplot as plt
import csv
import statistics
from boxplot import arquivo_csv
from boxplot import dados
#from boxplot import dados_limpos
from boxplot import arquivo_processo
import numpy as np

alt_masculino_2016 = []
alt_masculino_2014 = []
alt_masculino_2012 = []
alt_masculino_2010 = []
alt_masculino_2008 = []
alt_feminino_2016 = []
alt_feminino_2014 = []
alt_feminino_2012 = []
alt_feminino_2010 = []
alt_feminino_2008 = []

for i in arquivo_processo:
  dados.append(i)
dados_limpos = []
for i in range(len(dados)):
  if (dados[i][14] != 'NA' and dados[i][4] != 'NA' and dados[i][4] != 'Height' and dados[i][5] != 'NA' and dados[i][10] == 'Winter'):
    dados_limpos.append(dados[i])


for i in range(len(dados_limpos)):
  altura = float(dados_limpos[i][4])
  alt = round(altura/100)
  if (dados_limpos[i][2] == "M" and dados_limpos[i][9] == "2016"):
    alt_masculino_2016.append(alt)
  if (dados_limpos[i][2] == "M" and dados_limpos[i][9] == "2014"):
    alt_masculino_2014.append(alt)
  if (dados_limpos[i][2] == "M" and dados_limpos[i][9] == "2012"):
    alt_masculino_2012.append(alt)
  if (dados_limpos[i][2] == "M" and dados_limpos[i][9] == "2010"):
    alt_masculino_2010.append(alt)
  if (dados_limpos[i][2] == "M" and dados_limpos[i][9] == "2008"):
    alt_masculino_2008.append(alt)
  if (dados_limpos[i][2] == "F" and dados_limpos[i][9] == "2016"):
    alt_feminino_2016.append(alt)
  if (dados_limpos[i][2] == "F" and dados_limpos[i][9] == "2014"):
    alt_feminino_2014.append(alt)
  if (dados_limpos[i][2] == "F" and dados_limpos[i][9] == "2012"):
    alt_feminino_2012.append(alt)
  if (dados_limpos[i][2] == "F" and dados_limpos[i][9] == "2010"):
    alt_feminino_2010.append(alt)
  if (dados_limpos[i][2] == "F" and dados_limpos[i][9] == "2008"):
    alt_feminino_2008.append(alt)

def barrasf():
  x = [2016, 2014, 2012, 2010, 2008]
  yM = [statistics.mean(alt_masculino_2016 or [0]), statistics.mean(alt_masculino_2014 or [0]), statistics.mean(alt_masculino_2012 or [0]), statistics.mean(alt_masculino_2010 or [0]), statistics.mean(alt_masculino_2008 or [0])]
  yF = [statistics.mean(alt_feminino_2016 or [0]), statistics.mean(alt_feminino_2014 or [0]), statistics.mean(alt_feminino_2012 or [0]), statistics.mean(alt_feminino_2010 or [0]), statistics.mean(alt_feminino_2008 or [0])] 
  X_axis = np.arange(len(x))
  plt.bar(X_axis - 0.2, yM, 0.4,  label = 'Masculino',color='red')
  plt.bar(X_axis + 0.2, yF, 0.4, label = 'Feminino', color='blue')
  plt.xticks(X_axis, x)
  plt.title('Média ALT | 5 últimas edições de inverno | Medalhistas')
  plt.xlabel('Anos (edições)')
  plt.ylabel('Média ALT')
  plt.savefig('barras.png')
  plt.legend()
  plt.show()
  plt.close()


  