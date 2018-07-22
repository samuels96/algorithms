from nodes import Node

class d_list:
    def __init__(self):
        self.head = None

    def printall(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr = curr.next

    def insert_at_head(self,data):
        if self.head is None:
            self.head = Node(data)
            return
        node = Node(data)
        self.head.prev = node
        node.next = self.head
        self.head = node

    def insert_at_tail(self,data):
        node = Node(data)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        node.prev = curr

    def insert_after(self,locdata,data):
        node = Node(data)
        curr = self.head
        while curr.data != locdata and curr.next:
            curr = curr.next
        node.prev = curr
        node.next = curr.next
        node.next.prev = node
        curr.next = node

    def insert_at_pos(self,pos,data):
        node = Node(data)
        curr = self.head
        count = 1
        while count != pos and curr.next:
            curr = curr.next
            count += 1
        node.prev = curr
        node.next = curr.next
        node.next.prev = node
        curr.next = node

    def remove(self,locdata):
        curr = self.head
        if locdata == curr.data:
            curr.next.prev = None
            self.head = curr.next
            curr.next = None
            return
        while curr.next.data != locdata and curr.next:
            curr = curr.next
        curr.next = curr.next.next
        if curr.next:
            curr.next.prev = curr

    def reverse(self):
        temp = None
        curr = self.head
        while curr:
            temp = curr.prev
            curr.prev = curr.next
            curr.next = temp
            curr = curr.prev
        if temp:
            self.head = temp.prev
