class LinkedNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index):
        if index>=self.size:
            return -1
        else:
            temp = self.head
            for i in range(index):
                temp = temp.next
            return temp.val

    def addAtHead(self, val):
        self.head = LinkedNode(val, self.head)
        self.size += 1

    def addAtTail(self, val):
        if self.size==0:
            self.head = LinkedNode(val)
        else:
            temp = self.head
            while temp.next!=None:
                temp = temp.next
            temp.next = LinkedNode(val)
        self.size += 1

    def addAtIndex(self, index, val):
        if index<=self.size:
            if index==0:
                self.head = LinkedNode(val, self.head)
            else:
                temp = self.head
                prev = self.head
                for i in range(index):
                    prev = temp
                    temp = temp.next
                prev.next = LinkedNode(val, temp)
            self.size += 1
        

    def deleteAtIndex(self, index):
        if index<self.size:
            if index==0:
                self.head = self.head.next
            else:
                temp = self.head
                prev = self.head
                for i in range(index):
                    prev = temp
                    temp = temp.next
                prev.next = temp.next
            self.size -= 1