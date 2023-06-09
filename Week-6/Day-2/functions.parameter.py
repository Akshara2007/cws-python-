def greet(name):
    print(f"greeting to {name}")

def add(a,b,c):
    print(a+b+c)

def marks(phy,chem,sst,comp,eng):
    total =  phy + chem + sst + comp + eng
    print(total)
    print(total / 500 * 100)
    
greet("Akshara")
greet("xyz")
add(10,20,30)
marks(10,20,30,40,45)