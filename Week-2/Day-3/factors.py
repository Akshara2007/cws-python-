"""
Ask a number and print factors of that number.

16 -> 1,2,4,8,16
10 -> 1,2,5,10
25 -> 1,5,25

"""
num = int(input("enter the number = "))
count=0
for i in  range(1,num+1):
    if num%i==0:
       count=count+1
print(count)