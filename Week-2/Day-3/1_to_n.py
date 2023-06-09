"""
Ask a number from user

enter a number = 7

print 1 to N.

1 2 3 4 5 6 7 
"""
n=int(input("Enter a number"))
count=0
sum=0
for i in range(1,n+1):
     if i % 8 == 0:
        count=count+1#for count 
        sum= sum+1
print(count)


