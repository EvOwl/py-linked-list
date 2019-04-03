# -*- coding: utf-8 -*-

# Structure:
#                                    Linked List
#   _____________________________________/ \___________________________________
#  /                                                                           \
#   +--------/ node0 \-+    +--------/ node1 \-+           +--------/ nodeN \-+
#   +------------------+    +------------------+           +------------------+
#   | value: value     |    | value: value     |           | value: value     |
#   | next_node: next1 | => | next_node: node2 | => ... => | next_node: nodeN |
#   +------------------+    +------------------+           +------------------+
#


class ListNode:
    def __init__(self, value=None, next_node=None):
        self._value = value
        self._next_node = next_node

    def get_value(self):
        return self._value

    def get_next_node(self):
        return self._next_node

    def set_value(self, new_value):
        self._value = new_value

    def set_next_node(self, new_next_node):
        self._next_node = new_next_node


class SingleLinkedList:
    def __init__(self):
        self._head_list = None

    def add(self, value):
        pass

    def remove(self):
        pass

    def size(self):
        pass
