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

    def pop(self):
        element = self.stack.element
        self.stack = self.stack.next_node
        return element


def nearest_smallest_elements(l):
    stack = Stack()
    result = []
    for e in l:
        while not stack.is_empty():
            if stack.top() < e:
                break
            else:
                stack.pop()
        if stack.is_empty():
            result.append(-1)
        else:
            result.append(stack.top())
        stack.push(e)
    return result


print(nearest_smallest_elements([54, 39, 23, 72, 23, 41, 3, 3, 23, 12]))
