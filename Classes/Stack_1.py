stack=[55,43,22]
while True:
    print("1.Display the stack")
    print("2.Push the stack ")
    print("3.Remove the stack ")
    print("4.Peak the stack ")
    print("5.Check if the stack is empyt")
    print("6.Size of the stack")
    print("7.Exit")
    choice=int(input("Enter your choice = "))
    if choice==1:
        if len(stack)==0:
            print("Stack is empty")
        else:
            for i in stack:
                print(i,end=" ")
            print()
    elif choice == 2:
        num=int(input("Enter a number = "))
        stack.append(num)
        print(f"{num} has been added to stack")
    elif choice==3:
        # if len(stack)==0:
        #     print("Stack is empty")
        # else:
        #     n=stack.pop()
        #     print(f"{n} has been removed from stack")
        print("Stack is empty") if len(stack)==0 else print(f"{stack.pop()} has been removed from stack")
    elif choice==4:
        if len(stack)==0:
            print("Stack is empty")
        else:
            print(stack[-1])
    elif choice==5:
        if len(stack)==0:
            print("Stack is empty")
        else:
            print("Stack is not empty")
    elif choice == 6:
        if len(stack)==0:
            print("Stack is empty")
        else:
            print(f"Size of stack is {len(stack)}")
    elif choice==7:
        break
    else:
        print("Invalid")