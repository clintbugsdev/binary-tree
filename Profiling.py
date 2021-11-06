import cProfile
from LinkedList import LinkedList
from DoubleLinkedList import DoubleLinkedList


def profile_list_naive(n):
    l = list()
    for i in range(n):
        l.insert(0, i)


def profile_linked_list(n):
    ll = LinkedList()
    for i in range(n):
        ll.insert_start(i)


def profile_double_linked_list(n):
    dll = DoubleLinkedList()
    for i in range(n):
        dll.insert(i)


def profile(n):
    profile_list_naive(n)
    profile_linked_list(n)
    profile_double_linked_list(n)


cProfile.run("profile(100000)")
