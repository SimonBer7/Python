
class Leason:
    def __init__(self, id, name, teacher, class_name, floor_number, type):
        self.id = id
        self.name = name
        self.teacher = teacher
        self.class_name = class_name
        self.floor_number = floor_number
        self.type = type


    def __str__(self):
        print = str(self.id)+".) "+str(self.name)+", "+str(self.teacher)+", class: "+str(self.class_name)+", floor: "+str(self.floor_number)+", type: "+str(self.type)
        return print

    def basic_print(self):
        return self.name



