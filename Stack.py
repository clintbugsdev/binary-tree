from LinkedList import *


class Stack:
    def __init__(self):
        self.stack = LinkedList()

    def is_empty(self):
        return self.stack.is_empty()

    def push(self, element):
        self.stack.insert_head(element)

    def pop(self):
        return self.stack.delete_head()

    def reverse(self):
        return self.stack.reverse()

    def print_stack(self):
        self.stack.print_list()


class StackList:
    def __init__(self):
        self.stack = list()

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def print_stack(self):
        print(self.stack)


def use_stack():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.print_stack()
    s.pop()
    s.print_stack()


if __name__ == "__main__":
    use_stack()
