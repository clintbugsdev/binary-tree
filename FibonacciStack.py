import cProfile


class Node:
    def __init__(self, element=None, next_node=None):
        self.element = element
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.stack = None

    def is_empty(self):
        return self.stack is None

    def push(self, element):
        self.stack = Node(element, self.stack)

    def top(self):
        return self.stack.element

    def next(self):
        return self.stack.next_node.element

    def pop(self):
        element = self.stack.element
        self.stack = self.stack.next_node
        return element

    def reverse(self):
        prev = None
        current = self.stack
        while current is not None:
            next = current.next_node
            current.next_node = prev
            prev = current
            current = next
        self.stack = prev


def fib_stack(n):
    s = Stack()
    for i in range(1, n + 1):
        if i <= 2:
            s.push(1)
        else:
            s.push(s.top() + s.next())
    s.reverse()
    while not s.is_empty():
        s.pop()


def fib_list_as_stack_naive(n):
    s = list()
    for i in range(1, n + 1):
        if i <= 2:
            s.append(1)
        else:
            s.append(s[len(s) - 1] + s[len(s) - 2])
    s.reverse()
    while len(s) > 0:
        s.pop()


def profile(n):
    fib_stack(n)
    fib_list_as_stack_naive(n)


cProfile.run("profile(100000)")
