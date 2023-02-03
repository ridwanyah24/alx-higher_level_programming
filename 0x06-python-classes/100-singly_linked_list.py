#!/usr/bin/python3
"""Class Node that defines a node of a singly linked list"""

class Node:
    """The class node"""
    def __init__(self, data, next_node=None):

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next node must be a node object")
        self.__next_node = value

"""Class for a singly linked list"""

class SinglyLinkedList:
    """the class"""

    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        new_node = Node(value)

        if self.__head is None:
            new_node.next_node = None
            self.__head = new_node

        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            temp = self.__head
            while (temp.next_node is not None and temp.next_node.data < value):
                temp = temp.next_node
            new_node.next_node = temp.next_node
            temp.next_node = new_node

    def __str__(self):
        """Define the print representation of a singly linked lsit"""

        values = []
        temp = self.__head

        while temp is not None:
            values.append(str(temp.data))
            temp = temp.next_node
        return ('\n'.join(values))
