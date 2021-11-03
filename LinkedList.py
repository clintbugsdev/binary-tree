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

    def first_in(self, element):
        n = Node(element)
        if self.is_empty():
            self.head = self.tail = n
        else:
            n.next_node = self.head
            self.head = n

    def last_in(self, element):
        n = Node(element)
        if self.is_empty():
            self.head = self.tail = n
        else:
            self.tail.next_node = n
            self.tail = n

    def first_out(self):
        n = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = n.next_node
            n.next_node = None
        return n.element

    def print_list(self):
        n = self.head
        print("[", end="")
        while n is not None:
            print(n.element, " ", end="")
            n = n.next_node
        print("]")


def linked_list():
    ll = LinkedList()
    ll.first_in(30)
    ll.first_in(4)
    ll.first_in(13)
    ll.last_in(40)
    ll.last_in(60)
    ll.first_in(1)
    ll.print_list()
    ll.first_out()
    ll.first_out()
    ll.first_out()
    ll.first_out()
    ll.first_out()
    ll.first_out()
    ll.print_list()
    ll.first_in(3)
    ll.last_in(40)
    ll.last_in(41)
    ll.print_list()


if __name__ == "__main__":
    linked_list()
