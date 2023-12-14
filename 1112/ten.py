import threading
from queue import Queue

class BankovniUcet:
    def __init__(self, zustatek):
        self.zustatek = zustatek
        self.lock = threading.Lock()

    def vloz_mince(self, pocetKusu, mince):
        with self.lock:
            for i in range(0, pocetKusu):
                self.zustatek += mince

    def __str__(self):
        return "Bankovni ucet se zustatkem: {:d} CZK".format(self.zustatek)

def vloz_mince_thread(ucet, mince_queue):
    while True:
        pocetKusu, mince = mince_queue.get()
        if pocetKusu is None:
            break
        ucet.vloz_mince(pocetKusu, mince)
        mince_queue.task_done()

mujUcet = BankovniUcet(0)

mince_queue = Queue()

mince_queue.put((1000, 1))
mince_queue.put((1000, 2))
mince_queue.put((1000, 5))
mince_queue.put((1000, 10))
mince_queue.put((1000, 20))

# ThreadPool
num_threads = 4
threads = []

for _ in range(num_threads):
    thread = threading.Thread(target=vloz_mince_thread, args=(mujUcet, mince_queue))
    thread.start()
    threads.append(thread)

mince_queue.join()

for _ in range(num_threads):
    mince_queue.put((None, None))

for thread in threads:
    thread.join()

print(mujUcet)
