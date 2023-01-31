import threading #passso 1
import time


def main():
    threads = [
        threading.Thread(target=contar, args=('elefante',10)),
        threading.Thread(target=contar, args=('buraco',8)),
        threading.Thread(target=contar, args=('moeda',23)),
        threading.Thread(target=contar, args=('pato',12)),
        threading.Thread(target=contar, args=('gato',50))
    ] 
    #passso 2
    #adiciona a thread na pool de threads prontas para execução #passso 3
    [th.start() for th in threads] 
    print('podemos fazer outras coisas no programa enquanto a thread vai executando')
    print ('Douglas ' * 2)
    [th.join() for th in threads]  #avisa para ficar aguardando aqui até a thread terminar a execução #passso 4
    print ('pronto')


def contar(o_que, numero):
    for n in range(1, numero + 1):
        print(f'{n} {o_que}(s)...')
        time.sleep(1)

if __name__ == '__main__':
    main()
