from nodes import Node

class l_list:
    def __init__(self):
        self.head = None

    def printall(self):
        curr = self.head
        while curr:
            print(curr.data)
            curr=curr.next

    def insert_at_head(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insert_at_tail(self,data):
        node = Node(data)
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node

    def insert_after(self,locdata,data):
        node = Node(data)
        curr = self.head
        while curr.data != locdata and curr.next:
            curr = curr.next
        node.next = curr.next
        curr.next = node

    def insert_at_pos(self,pos,data):
        node = Node(data)
        curr = self.head
        count = 1
        while count != pos and curr.next:
            curr = curr.next
            count += 1
        node.next = curr.next
        curr.next = node

    def remove(self,locdata):
        curr = self.head
        if locdata == curr.data:
            self.head = curr.next
            curr.next = None
            return
        while curr.next.data != locdata and curr.next:
            curr = curr.next
        curr.next = curr.next.next

    def reverse(self):
        curr = self.head
        self.head = None
        while curr:
            curr.next,curr,self.head = self.head,curr.next,curr
