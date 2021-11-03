from LinkedList import *


class Queue:
    def __init__(self):
        self.queue = LinkedList()

    def is_empty(self):
        return self.queque.is_empty()

    def enqueue(self, element):
        self.queue.first_in(element)

    def dequeue(self):
        return self.queue.first_out()

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


def use_queue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.print_queue()
    q.dequeue()
    q.dequeue()
    q.print_queue()


if __name__ == "__main__":
    use_queue()
