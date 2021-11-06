class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    # 0(1) time complexity
    def insert_start(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

        self.num_of_nodes += 1

    # linear running time 0(N) complexity
    def insert_end(self, data):
        new_node = Node(data)

        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

        self.num_of_nodes += 1

    def size_of_list(self):
        return self.num_of_nodes

    # linear running time 0(N) complexity
    def traverse(self):

        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data)
            actual_node = actual_node.next_node

    def remove(self, data):

        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node is not None:
            if actual_node.data == data:
                break
            else:
                previous_node = actual_node
                actual_node = actual_node.next_node

        # search missed - the item is not present
        if actual_node is None:
            return

        # usually if the data was in the head node
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            previous_node.next_node = actual_node.next_node

        # decrease number of nodes
        self.num_of_nodes -= 1


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_start(1)
    ll.insert_start(2)
    ll.insert_start(3)
    ll.insert_start(4)
    ll.traverse()
    ll.remove(4)
    print("----")
    ll.traverse()
    print("----")
    print(ll.size_of_list())
