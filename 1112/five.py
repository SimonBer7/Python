
import multiprocessing
import time

nakupniSeznam = ["Mleko","Maslo","Rohlik"]

def vypisNakupniSeznam():
    for food in nakupniSeznam:
        print(food)
        time.sleep(1)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=vypisNakupniSeznam)
    p1.start()
    p1.join()
