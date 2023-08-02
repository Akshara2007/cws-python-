class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None

    def traversal(self):
        if self.head==None:
            print("Cannot traverse, linked list is empty")
        else:
            node=self.head
            while True:
                print(node.value,end=" ")
                node=node.next
                if node==None:
                    break


singlyLinkedList=SLinkedList()
node1=Node(34)
node2=Node(11)
node3=Node(100)

singlyLinkedList.head=node1
singlyLinkedList.tail=node3
singlyLinkedList.head.next=node2
singlyLinkedList.head.next.next=node3

singlyLinkedList.traversal()

# singlyLinkedList=SLinkedList()
# node1=Node(44)
# singlyLinkedList.head=node1
# singlyLinkedList.tail=node1
# singlyLinkedList.traversal()

"""
FOR 2 NODES
singlyLinkedList=SLinkedList()
node1=Node(54)
node2=Node(12)

singlyLinkedList.head=node1
singlyLinkedList.tail=node2
singlyLinkedList.head.next=node2
singlyLinkedList.traversal()

# print(singlyLinkedList.tail.value)
# print(singlyLinkedList.head.next.value)
# print(singlyLinkedList.tail)
"""