a={}

name=input("enter the name = ")
age=input("enter the age = ")
gender=input("enter the gender = ")
a["name"]=name
a["age"]=age
a["gender"]=gender

for i in range(0,5):
    sub=input("Enter subject name=")
    marks=int(input("Enter marks of the subject = "))
    a[sub]=marks

print(a)