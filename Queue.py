from LinkedList import *


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def is_empty(self):
        return self.queue.is_empty()

    def enqueue(self, element):
        self.queue.insert_tail(element)

    def dequeue(self):
        return self.queue.delete_head()

    def reverse(self):
        return self.queue.reverse()

    def print_queue(self):
        return self.queue.print_list()


class QueueList:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self, element):
        self.queue.insert(0, element)

    def dequeue(self):
        return self.queue.pop()

    def print_queue(self):
        print(self.queue)


def reverse_linked_list():
    ll = LinkedList()
    ll.insert_first(30)
    ll.insert_first(4)
    ll.insert_first(13)
    ll.insert_first(3)
    ll.insert_first(5)
    ll.print_list()
    ll2 = LinkedList()
    while not ll.is_empty():
        ll2.insert_first(ll.delete_first())
    ll2.print_list()


def use_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.print_queue()
    q.dequeue()
    q.print_queue()


if __name__ == "__main__":
    use_queue()
