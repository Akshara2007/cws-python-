"""
Exception Handling
"""

try:
    a=int(input("Enter a number = "))
    b=int(input("Enter a number = "))
    print(a/b)
except:
    print("Some error occurenced")
else:
    print("This is a else statement")
finally:
    print("This is a else statement")