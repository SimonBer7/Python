from five import SchoolProfile
import pickle

adam = SchoolProfile("Adam", "Schorny", "ada123", "Matematika", "SPSS Dusni", "Jan Zeleny")

def add_profile():
    with open("school.dat", "ab") as file:
        pickle.dump(adam, file)

def load_profile():
    with open("school.dat", "rb") as file:
        friend = pickle.load(file)
        print(friend.toString())


try:
    add_profile()
    load_profile()
except:
    print("error")
