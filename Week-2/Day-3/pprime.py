"""
Ask a number from user.

Check if the number is prime or not.
"""
num=int(input("enter a number= "))
count=0
for i in range (1, num+1):
    if num % i ==0:
        print(i, end=" ")
        count=count + 1

print()
print(count)

if count==2:
    print("It is a prime number")
else:
    print("It is a composite number")