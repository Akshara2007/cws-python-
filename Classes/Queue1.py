Queue = []
while True:
    print("1.Display the Queue")
    print("2.Enqueue the Queue ")
    print("3.Dequeue the Queue ")
    print("4.Front the Queue ")
    print("5.Rear the queue")
    print("6.check if the queue is empyt or not")
    print("7.Size of the Queue")
    print("8.Exit")
    choice=int(input("Enter your choice = "))
    if choice == 1:
         if len(Queue)==0:
            print("Queue is empty")
         else:
            for i in Queue:
                print(i,end=" ")
            print()
    elif choice == 2:
        num=int(input("Enter a number = "))
        Queue.append(num)
        print(f"{num} has been enqueued to the queue")
    elif choice == 3:
          print("Queue is empty") if len(Queue)==0 else print(f"{Queue.pop(0)} has been Dequeued from the queue")
    elif choice == 4:
        if len(Queue) == 0:
            print("Queue is empty")
        else:
            print(f"Front of Queue is : {Queue[0]}")
    elif choice == 5:
        print("Queue is empty") if len(Queue) == 0 else print(f"Rear of Queue is: {Queue[-1]}")
    elif choice == 6:
        print(f"Size of Queue : {len(Queue)}")
    elif choice == 7:
        if len(Queue)==0:
            print("Queue is empty")
        else:
            print("Queue is not empty")
    elif choice == 8:
        print("exiting")
        break