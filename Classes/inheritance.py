class Parent:
    def setParentInfo(self): 
        self.fatherName = input("Enter father name = ")

    def displayParent(self):
        print("Display of Parent class is being called")
        print(self.fatherName)


class Child(Parent):
    def setChildInfo(self):
        self.childName = input("Enter child name = ")

    def displayChild(self):
        print("Display of Child class is being called")

    def displayAllInfo(self):
        print(f"Father name = {self.fatherName}")
        print(f"Child name = {self.childName}")


o = Child()
o.setParentInfo()
o.setChildInfo()
o.displayAllInfo()