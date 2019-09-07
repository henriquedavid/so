import posix_ipc
import signal
import threading
import time


def add(val1, val2, valor):
    valor = val1 * val2
    return valor


def calculaLineByCol(matrizA, matrizB, matrizResult):
        self_t = threading.currentThread()
        print(self_t.ident)
        for e in range(0, len(matrizB[0])):
                soma = 0
                for k in range(0, len(matrizA[0])):
                    soma += add(matrizA[i][k], matrizB[k][e], soma)
                matrizResult[i][e] = soma


matrizA = [[3, 0, 2],
           [9, 1, 7],
           [1, 0, 1]]
matrizB = [[1, 0, -2],
           [-2, 1, -3],
           [-1, 0, 3]]

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
    t1 = threading.Thread(target=calculaLineByCol, args=(matrizA, matrizB, matrizResult))
    t1.start()
    threads.append(t1)

    for e in threads:
        e.join()

print("Decorrido em paralelo: ", time.time()-t)
print(matrizResult)
