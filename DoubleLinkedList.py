class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # this operation inserts items at the end of the linked list
    # so we have to manipulate the tail node in 0(1) running time
    def insert(self, data):

        new_node = Node(data)

        # when the list is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # there is at least 1 item in the data structure
        # we keep inserting items at the end of the linked list
        else:
            # [1]<-[2]
            new_node.previous = self.tail
            # [1]->[2]
            self.tail.next = new_node
            # [1]<->[2]
            self.tail = new_node

    # we can travers a doubly linked list in both directions
    def traverse_forward(self):

        actual_node = self.head

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.next

    def traverse_backward(self):

        actual_node = self.tail

        while actual_node is not None:
            print("%d" % actual_node.data)
            actual_node = actual_node.previous


if __name__ == "__main__":
    dll = DoubleLinkedList()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.traverse_forward()
