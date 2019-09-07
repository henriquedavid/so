import time
import random
#matrizA = [[3,0,2],[9,1,7],[1,0,1]]
#matrizB = [[1,0,-2],[-2,1,-3],[-1,0,3]]
matrizA = [[2,1,4], [0,1,1]]
matrizB = [[6,3,-1,0], [1,1,0,4], [-2,5,0,2]]

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

#matrizResult = [[9,9,9],[9,9,9],[9,9,9]]
    matrizResult = []

    for i in range(0, len(matrizA)):
        tabela1 = []
        for e in range(0, len(matrizB[0])):
            tabela1.append(0)
        matrizResult.append(tabela1)

    if len(matrizA[0]) != len(matrizB):
        print("O numero de linha da matriz A tem que ser igual a da matriz B!")
    else:
        t = time.time()
        for i in range(0,len(matrizA)):
            for e in range(0, len(matrizB[0])):
                matrizResult[i][e] = 0

        aux = 0
        for i in range(0,len(matrizA)):
            for e in range(0, len(matrizB[0])):
                soma = 0
                for k in range(0, len(matrizA[0])):
                    soma += matrizA[i][k] * matrizB[k][e]
                matrizResult[i][e] = soma

        print("Matriz: ", q ," Decorrido: " , time.time() - t)

    #print(matrizResult)