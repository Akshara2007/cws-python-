"""
Ask two numbers from user-> start,end
"""
Start=int(input("enter start number="))
end=int(input("enter end number="))

i = Start
total =0 
while i <= end:
    if i%4==0:
         total = total + i
    i = i + 1
print(total)
                 