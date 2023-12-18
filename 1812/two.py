

def read_all():
    with open("helloworld.txt", "r") as file:
        return file.read()

def read_one_line():
    with open("helloworld.txt", "r") as file:
        return file.readline()

def read_by_par(par):
    with open("helloworld.txt", "r") as file:
        tmp = ""
        for i in range(par):
            tmp += str(i+1)+"."+str(file.readline())
        return tmp



print(read_by_par(3))
