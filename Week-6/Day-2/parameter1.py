# calculate the sum of two  list
def sumOflist(a,b):
    print(sum(a) + sum (b))

def marks(phy,chem,sst,comp,eng):
    total =  phy + chem + sst + comp + eng
    print(total)
    print(total / 500 * 100)

# named parameter
marks(eng = 100 , phy = 50 , chem = 60 , sst = 45,comp = 79)
print(marks)
#sumOflist([43,12,3,44,55,44],[66,55,44])
#sumOflist()