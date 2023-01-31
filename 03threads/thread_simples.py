import threading #passso 1
import time


def main():
    th = threading.Thread(target=contar, args=('elefante',10)) #passso 2

    th.start() #adiciona a thread na pool de threads prontas para execução #passso 3
    print('podemos fazer outras coisas no programa enquanto a thread vai executando')
    print ('Douglas ' * 2)
    th.join() #avisa para ficar aguardando aqui até a thread terminar a execução #passso 4
    print ('pronto')


def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)

if __name__ == '__main__':
    main()
