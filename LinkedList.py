class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def insert_head(self, element):
        n = Node(element)
        if self.is_empty():
            self.head = self.tail = n
        else:
            n.next_node = self.head
            self.head = n

    def insert_tail(self, element):
        n = Node(element)
        if self.is_empty():
            self.head = self.tail = n
        else:
            self.tail.next_node = n
            self.tail = n

    def delete_head(self):
        if self.is_empty():
            return
        else:
            n = self.head
            if self.head == self.tail:
                self.head = self.tail = None
            else:
                self.head = n.next_node
                n.next_node = None
            return n.element

    def reverse(self):
        prev = None
        current = self.head
        while current is not None:
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        self.head = prev

    def print_list(self):
        n = self.head
        print("[", end="")
        while n is not None:
            print(n.element, " ", end="")
            n = n.next_node
        print("]")


def linked_list():
    ll = LinkedList()
    ll.insert_head(1)
    ll.insert_head(2)
    ll.insert_head(3)
    ll.insert_head(4)
    ll.insert_head(5)
    ll.print_list()
    ll.delete_head()
    ll.delete_head()
    ll.delete_head()
    ll.delete_head()
    ll.delete_head()
    ll.delete_head()
    ll.print_list()


if __name__ == "__main__":
    linked_list()
