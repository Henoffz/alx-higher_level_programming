#!/usr/bin/python3


class Node:
    """ node class singly lists model"""
    def __init__(self, data, next_node=None):
        """initializing obj of the node class"""
        self.__data = None
        self.__next_node = None
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly-linked lists class"""
    def __init__(self):
        """initializing the obj of a singly lists"""
        self.__head = None

    def __str__(self):
        """prints the linked lists"""
        tmp = self.__head
        n_list = []
        while tmp is not None:
            n_list.append(str(tmp.data))
            tmp = tmp.next_node
        return ("\n".join(n_list))

    def sorted_insert(self, value):
        """insert the obj node"""
        new_node = Node(value)

        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node
