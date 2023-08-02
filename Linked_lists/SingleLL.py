class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traversal(self):
        if self.head == None:
            print("Cannot traverse, linked list is empty")
        else:
            node = self.head
            while True:
                print(node.value, end=" ")
                node = node.next
                if node == None:
                    break

    def insertSLL(self, value, location):  # 0,-1
        newNode = Node(value)
        if self.head == None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
                newNode.next = self.head
                self.head = newNode
            elif location == -1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    if tempNode.next == None:
                        print("Cannot add, because location out of index")
                        return
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode

    def searchSLL(self, nodeValue):
        if self.head == None:
            print("SLL is empty")
        else:
            node = self.head
            while True:
                if node == None:
                    print("Not found")
                    break
                if node.value == nodeValue:
                    print("Found")
                    return
                node = node.next

    def deleteLinkedList(self):
        self.head = None
        self.tail = None

    def deleteNode(self, location):
        if self.head == None:
            print("Cannot delete, Linked list is empty")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while True:
                        if node == None:
                            break
                        if node.next == self.tail:
                            node.next = None
                            self.tail = node
                            break
                        node = node.next
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    if tempNode.next == None:
                        print("Cannot add, because location out of index")
                        return
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = nextNode.next


singlyLinkedList = SLinkedList()
singlyLinkedList.insertSLL(100, 0)
singlyLinkedList.insertSLL(200, 0)
singlyLinkedList.insertSLL(50, -1)
singlyLinkedList.insertSLL(45, -1)
singlyLinkedList.insertSLL(12, -1)
singlyLinkedList.insertSLL(3444, -1)
singlyLinkedList.insertSLL(4000, -1)
singlyLinkedList.insertSLL(15, 0)
singlyLinkedList.traversal()
print()
# singlyLinkedList.searchSLL(1000)
# singlyLinkedList.deleteNode(0)
# singlyLinkedList.deleteNode(-1)
singlyLinkedList.deleteNode(2)
print()
singlyLinkedList.traversal()
print()
singlyLinkedList.deleteNode(3)
singlyLinkedList.traversal()
singlyLinkedList.deleteLinkedList()
print()
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
