import threading
import time
import random

def add(val1, val2, valor):
    valor = val1 * val2
    return valor


def calculaLineByCol(matrizA, matrizB, matrizResult, i_posic):
        for e in range(0, len(matrizB[0])):
                soma = 0
                for k in range(0, len(matrizA[0])):
                    soma += add(matrizA[i_posic][k], matrizB[k][e], soma)
                matrizResult[i_posic][e] = soma


#matrizA = [[3, 0, 2],
#           [9, 1, 7],
#           [1, 0, 1]]
#matrizB = [[1, 0, -2],
#           [-2, 1, -3],
#           [-1, 0, 3]]

#matrizA = [[2,1,4], [0,1,1]]
#matrizB = [[6,3,-1,0], [1,1,0,4], [-2,5,0,2]]

#logica para gerar as matrizes aleatoriamente
tamanhos = [1, 2,3,4,5,6,8,10,20,30,40,50,75,100]

for q in tamanhos:
    matrizA = []
    for i in range(0, q):
        linha = []
        for o in range(0, q):
            linha.append(random.randint(1,100))
        matrizA.append(linha)

    matrizB = []
    for i in range(0, q):
        linha = []
        for o in range(0, q):
            linha.append(random.randint(1,100))
        matrizB.append(linha)
    

    #matrizResult = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]
    matrizResult = []

    for i in range(0, len(matrizA)):
        tabela1 = []
        for e in range(0, len(matrizB[0])):
            tabela1.append(0)
        matrizResult.append(tabela1)

    # define uma lista de threads que serao executadas
    threads = []
    t = time.time()

    for i in range(0, len(matrizA)):
        # para cada linha da matriz chama uma thread para executar a linha
        t1 = threading.Thread(target=calculaLineByCol, args=(matrizA, matrizB, matrizResult, i))
        t1.start()
        threads.append(t1)

    for e in threads:
        e.join()

    threads = []
    print("Matriz: ", q , " Decorrido em paralelo: ", time.time()-t)