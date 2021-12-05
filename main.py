# Importação de módulos ou pacotes #
import matplotlib.pyplot as plt
import time as t
import os
from boxplot import boxplotf
from linhas import linhasf
####################################

# Variáveis #
option = ""

#############


# Funções para a execução do menu #
def menu():
    print("=-=" * 10)
    print("Digite |L| para exibir gráfico de linhas.")
    print("Digite |B| para exibir gráfico de barras.")
    print("Digite |X| para exibir gráfico de boxplot.")
    print("Digite |T| para a resposta textual.")
    print("Digite |A| para a imprimir arquivo.")
    print("Digite |Q| para sair do programa.")
    print("=-=" * 10)
    option = input("=> ")
    option = option.lower()
    if (option != 'a' and option != 'b' and option != 'l' and option != 'x'
            and option != 'q' and option != 't'):
        os.system('clear')
        print("Digite uma letra acima que seja válida!")
        t.sleep(2)
        os.system('clear')
    if (option == 'q'):
        os.system('clear')
        print("Programa finalizado.")
        t.sleep(1)
        return "q"
    if (option == 'x'):
      boxplotf()
    if (option == 'l'):
      linhasf()


###################################

# Execução do programa #
while (option != "q"):
    option = menu()
########################
