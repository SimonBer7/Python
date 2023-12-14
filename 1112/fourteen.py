from time import sleep
from threading import Thread
from queue import Queue

def producent(queue):
    print('Producent zacal')
    for pismeno in ["a", "h", "o", "j", "s", "v", "e", "t", "e"]:
        while queue.qsize() >= 3:
            sleep(0.1)
        queue.put(pismeno)
        print("Producent vlozil do fronty pismeno : {}".format(pismeno))
        sleep(0.5)

    queue.put(-1)  # Vlozeni -1 znamena ukonceni
    print('Producent skoncil')

def konzument(queue):
    print('Konzument zacal')
    while True:
        while queue.qsize() == 0:
            sleep(0.1)
        pismeno = queue.get()
        if pismeno == -1:  # Pokud je to -1, znamena to ukonceni
            break
        sleep(1)
        print("Konzument nacetl : {}".format(pismeno))
    print('Konzument skoncil')

if __name__ == "__main__":
    queue = Queue()

    konzument = Thread(target=konzument, args=(queue,))
    producent = Thread(target=producent, args=(queue,))

    konzument.start()
    producent.start()

    producent.join()
    konzument.join()
