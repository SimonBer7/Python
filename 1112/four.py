import time
import multiprocessing

class VypisCiselProcess(multiprocessing.Process):
    def __init__(self, od, do):
        super(VypisCiselProcess, self).__init__()
        if (isinstance(od and do, int)):
            self.od = od
            self.do = do
        else:
            raise ValueError("Error :(")

    def run(self):
        for i in range(self.od, self.do):
            print(i)
            time.sleep(1)


if __name__ == "__main__":
  print("ZACATEK PROGRAMU")
  p1 = VypisCiselProcess(1, 5)
  p1.start()
  p1.join()
  print("KONEC PROGRAMU")



