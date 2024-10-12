class Information:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ",self.name)
        print("Age: " , self.age)


class Student(Information):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.qal = None
        self.marks = None

    def set_data(self, marks, qal):
        self.marks= marks
        self.qal = qal
    def display_new(self):
        print("Marks: ",self.marks)
        print("Qal: ",self.qal)


# obj1 = Information("Mandeep", 29)
# obj1.display(



obj1 = Student("Mandeep",29)
obj1.set_data(100,"Btech")
obj1.display()
