from boxplot import arquivo_csv
from boxplot import dados
#from boxplot import dados_limpos
from boxplot import arquivo_processo
import time as t

nomes = []

for i in arquivo_processo:
  dados.append(i)
dados_limpos = []
for i in range(len(dados)):
  if (dados[i][13] == "Speed Skating Women's 500 metres" and dados[i][14] == 'Gold'):
    dados_limpos.append(dados[i])

for i in range(len(dados_limpos)):
  nomes.append(dados_limpos[i][1])

nomes_limpos = set(nomes)
def resptextualf():
  print("===== Atletas que ganharam ouro no Speed Skating Women's 500 metres =====")
  t.sleep(2)
  print(nomes_limpos)
  t.sleep(2)