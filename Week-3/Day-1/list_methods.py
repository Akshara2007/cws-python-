#a=[45,32,12,33,43,11]
#b=[100,200]
#print(a)

#add 100 to end of the list
#a.append(100)
#a .append(50)
#a .append(1)
#print(a and b)
#append means to appear

#a.insert(-1,100)
#print(a)

#a.pop()
#pop is for  remove from postion 
#print(a)

#a.remove(12)
#print(a)

"""
Ask a number from user
"""
#a=[445,74,51]
#num=int(input("Enter a number="))
#a.append(num)
#print(a)

""" 
ask anumber and posyion from user
"""
a=[445,74,51]
num=int(input("Enter a number = "))
postion=int(input("Enter a postion = "))
a.insert(postion,num)
print(a)