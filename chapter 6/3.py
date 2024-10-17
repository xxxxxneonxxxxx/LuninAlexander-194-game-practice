class Node:
    def __init__(self, data=None):
        self.data = data
        self.next =None


class LinkedList:
    def __init__(self):
        self.head =None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        if self.is_empty():
            self.head=Node(data)
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=Node(data)
    def prepend(self, data):
        if self.is_empty():
            self.head=Node(data)
            return
        cur=self.head
        while cur.next:
            cur=cur.next
        cur.next=Node(data)
    def delete(self, data):
        if self.is_empty():
            return
        if self.head.data==self.head:
            return
        while self.next.next and self.next.data !=data:
            self.head=self.head.next
        if self.head.next:
            self.head.next = self.head.next.next

    def display(self):
# Example usage:
my_linked_list = LinkedList()

my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.prepend(0)

my_linked_list.display()

my_linked_list.delete(2)

my_linked_list.display()