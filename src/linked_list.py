# -*- coding: utf-8 -*-
import sys

class Node(object):
    """This sets our Node class"""
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList(object):
    def __init__(self, data):
        self.head = None
        try:
            if data:
                for item in data:
                    self.push(item)
        except TypeError:
            print('Please enter an iterable object.')


    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node
        return self.head

    def pop(self):
        pop_node = self.head
        self.head = self.head.next_node
        return pop_node

    # def size()
    #
    # def search(data)
    #
    # def remove(node)
    #
    # def display()

# if __name__ == '__main__':
#     LinkedList(sys.argv[1])
