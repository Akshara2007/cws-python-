"""
find sum of all numbers divisible by 7 from 1 to 50
"""
start=int(input("enter the number =  "))
end=int(input("enter the number =  "))
i =start
total = 0
while i <= end:
     if i%4 == 0:
          total=total + i
          i = i + 1

print(total) 