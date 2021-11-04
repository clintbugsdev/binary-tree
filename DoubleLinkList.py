class Node:
    def __init__(self, element=None):
        self.element = element
        self.next_node = None
        self.prev_node = None


class DoubleLinkList:
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
            self.head.prev_node = n
            n.next_node = self.head
            self.head = n

    def insert_tail(self, element):
        n = Node(element)
        if self.is_empty():
            self.head = self.tail = n
        else:
            n.prev_node = self.tail
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
                self.head.prev_node = None
                n.next_node = None
            return n.element

    def print_list(self):
        n = self.head
        print("[", end="")
        while n is not None:
            print(n.element, " ", end="")
            n = n.next_node
        print("]")
        print("[", end="")
        m = self.tail
        while m is not None:
            print(m.element, " ", end="")
            m = m.prev_node
        print("]")


def double_linked_list():
    dll = DoubleLinkList()
    dll.insert_tail(1)
    dll.insert_tail(2)
    dll.insert_tail(3)
    dll.insert_tail(4)
    dll.insert_tail(5)
    dll.delete_head()
    dll.delete_head()
    dll.delete_head()
    dll.delete_head()
    dll.delete_head()
    dll.delete_head()
    dll.print_list()


if __name__ == "__main__":
    double_linked_list()
