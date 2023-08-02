class Parent:
    def __init__(self):
        self.fatherName = input("Enter father name = ")
        self.motherName = input("Enter mother name = ")

    def dis(self):
        print("This is dis method")


class Child(Parent):
    def __init__(self):
        self.childName = input("Enter child name = ")
        super().__init__()

    def displayAll(self):
        print(f"fatherName = {self.fatherName}")
        print(f"motherName = {self.motherName}")
        print(f"childName = {self.childName}")


o = Child()
o.displayAll()

p = Child()
p.displayAll()