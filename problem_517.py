"""
Given two singly linked lists that intersect at some point, find the intersecting node. The lists are non-cyclical.
For example, given A = 3 -> 7 -> 8 -> 10 and B = 99 -> 1 -> 8 -> 10, return the node with value 8.
In this example, assume nodes with the same value are the exact same node objects.
Do this in O(M + N) time (where M and N are the lengths of the lists) and constant space.

"""
import copy
class LinkedList:
    def __init__(self):
        self.head = None

class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None

def getIntersectNode(A, B):
    new_A = copy.copy(A)
    new_B = copy.copy(B)
    while new_B.head != None:
        new_A = copy.copy(A)
        while new_A.head != None:
            if new_A.head.value == new_B.head.value:
                return new_A.head.value
            else:
                new_A.head = new_A.head.next
        new_B.head = new_B.head.next
    return "No intersection found"



if __name__=="__main__":
    node1_a = Node(3)
    node2_a = Node(7)
    node3_a = Node(8)
    node4_a = Node(10)

    node1_a.next = node2_a
    node2_a.next = node3_a
    node3_a.next = node4_a

    A = LinkedList()
    A.head = node1_a

    node1_b = Node(99)
    node2_b = Node(1)
    node3_b = Node(8)
    node4_b = Node(10)

    node1_b.next = node2_b
    node2_b.next = node3_b
    node3_b.next = node4_b

    B = LinkedList()
    B.head = node1_b

    print (getIntersectNode(A, B))

