import django


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def createDoublyLinkedList(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode

    def traversal(self):
        if self.head == None:
            print("Cannot traverse, doubly linked list is empty")
        else:
            tempNode = self.head
            while True:
                if tempNode == None:
                    break
                print(tempNode.value, end=" ")
                tempNode = tempNode.next
            print()

    def searchNode(self, value):
        if self.head == None:
            print("Cannot traverse, doubly linked list is empty")
        else:
            tempNode = self.head
            while True:
                if tempNode == None:
                    print("Not found")
                    return
                if tempNode.value == value:
                    print("Found")
                    return
                tempNode = tempNode.next

    def reverseTraversal(self):
        if self.head == None:
            print("Cannot traverse, doubly linked list is empty")
        else:
            tempNode = self.tail
            while True:
                if tempNode == None:
                    break
                print(tempNode.value, end=" ")
                tempNode = tempNode.prev
            print()

    def deleteNode(self, location):
        if self.head == None:
            print("Cannot delete, Doubly Linked List is empty.")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head.next.prev = None
                    self.head = self.head.next
            elif location == -1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail.prev.next = None
                    self.tail = self.tail.prev
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    if tempNode.next == None:
                        print("Cannot delete, because location is out of index")
                        return
                    tempNode = tempNode.next
                    index += 1
                tempNode.next.next.prev = tempNode
                tempNode.next = tempNode.next.next

    def insertDLL(self, value, location):
        newNode = Node(value)
        if self.head == None:
            print("Cannot insert.")
        else:
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode


doublyLL = DoublyLinkedList()
doublyLL.createDoublyLinkedList(100)
doublyLL.insertDLL(5, 0)
doublyLL.insertDLL(55, 0)
doublyLL.insertDLL(99, -1)
doublyLL.insertDLL(150, -1)
doublyLL.insertDLL(33, 2)
doublyLL.traversal()
doublyLL.deleteNode(5)
doublyLL.traversal()
# doublyLL.deleteNode(0)
# doublyLL.deleteNode(2)
# doublyLL.traversal()
# doublyLL.searchNode(1000)
# doublyLL.reverseTraversal()
