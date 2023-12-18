import multiprocessing
import time

def worker():
    while True:
        pass

if __name__ == "__main__":
    num_cores = multiprocessing.cpu_count()
    processes = []

    for _ in range(num_cores):
        process = multiprocessing.Process(target=worker)
        process.start()
        processes.append(process)

    # Necháme program běžet po dobu 5 sekund
    time.sleep(50)

    # Zastavíme všechny procesy
    for process in processes:
        process.terminate()
        process.join()

    print("Zatížení procesorových jader bylo ukončeno.")
