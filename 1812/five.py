

class SchoolProfile:
    def __init__(self, jmeno, prijmeni, username, favorite_school_subject, favorite_school, favorite_teacher):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.username = username
        self.favorite_school_subject = favorite_school_subject
        self.favorite_school = favorite_school
        self.favorite_teacher = favorite_teacher


    def toString(self):
        return self.jmeno+" "+self.prijmeni+" | username: "+self.username+", "+self.favorite_school_subject+", "+self.favorite_school+", "+self.favorite_teacher


