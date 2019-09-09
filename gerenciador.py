import threading
import time

line = -1
column = -1
lock = threading.Lock()
cal = True
pr = True

def add(val1, val2, valor):
    valor = val1 * val2
    return valor


def calculaLineByCol(matrizA, matrizB, matrizResult, i_posic, cal_):
        global line
        global column
        global Lock
        global cal
        global pr 
        while(cal):
                if(line != -1 and column != -1):
                        lock.acquire()
                        for e in range(0, len(matrizB[0])):
                                soma = 0
                                for k in range(0, len(matrizA[0])):
                                        soma += add(matrizA[i_posic][k], matrizB[k][e], soma)
                                matrizResult[i_posic][e] = soma
                        if(pr):
                                print(matrizResult[line][column])
                                pr = False
                        line = -1
                        column = -1
                        lock.release()
        


#matrizA = [[3, 0, 2],
#           [9, 1, 7],
#           [1, 0, 1]]
#matrizB = [[1, 0, -2],
#           [-2, 1, -3],
#           [-1, 0, 3]]
def calc():
        matrizA = [[2,1,4], [0,1,1]]
        matrizB = [[6,3,-1,0], [1,1,0,4], [-2,5,0,2]]

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

        '''for e in threads:
                e.join()

        print("Decorrido em paralelo: ", time.time()-t)
        print(matrizResult)'''

def main():
        key = True
        global line
        global column
        global cal
        global pr
        pr = False

        matrizA = [[2,1,4], [0,1,1]]
        matrizB = [[6,3,-1,0], [1,1,0,4], [-2,5,0,2]]

        #matrizResult = [[9, 9, 9], [9, 9, 9], [9, 9, 9]]
        matrizResult = []

        # define uma lista de threads que serao executadas
        threads = []
        t = time.time()

        for i in range(0, len(matrizA)):
                tabela1 = []
                for e in range(0, len(matrizB[0])):
                        tabela1.append(0)
                matrizResult.append(tabela1)
        
        for i in range(0, len(matrizA)):
                # para cada linha da matriz chama uma thread para executar a linha
                t1 = threading.Thread(target=calculaLineByCol, args=(matrizA, matrizB, matrizResult, i, cal))
                t1.start()
                threads.append(t1)

        while(key):
                if(not pr):
                        entrada = input("Deseja continuar com o programa? - S para sim, qualquer outra tecla pra não ")
                        if entrada == 'S':
                                line = int(input("Digite linha que deseja executar "))
                                column = int(input("Digite coluna que deseja executar "))
                                pr = True
                        else:

                                print("Decorrido em paralelo: ", time.time()-t)
                                print(matrizResult)
                                cal = False
                                for e in threads:
                                        e.join()
                                exit(1)
                
if __name__ == '__main__':
    main()
