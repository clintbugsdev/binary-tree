class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    # 0(n) linear running time complexity
    def get_middle_node(self):

        slow_pointer = fast_pointer = self.head

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node
            slow_pointer = slow_pointer.next_node

        return slow_pointer

    def insert(self, data):

        new_node = Node(data)

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

        self.size += 1


if __name__ == "__main__":

    ll = LinkedList()

    ll.insert(10)
    ll.insert(20)
    ll.insert(30)

    print(ll.get_middle_node().data)
