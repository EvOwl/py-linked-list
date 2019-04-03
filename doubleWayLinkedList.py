# -*- coding: utf-8 -*-
from doubleListNode import DoubleListNode


class LinkedList:
    def __init__(self):
        self._head_node = None
        self._tail_node = None

    def get_head_list(self):
        return self._head_node

    def get_tail_list(self):
        return self._tail_node

    def add_node_head(self, value):
        temp = DoubleListNode(value)
        if self._head_node is None:
            temp.set_next_node(temp)
            self._tail_node = temp
        else:
            self._head_node.set_next_node(temp)
            temp.set_prev_node(self._head_node)
        self._head_node = temp

    def add_node_tail(self, value):
        temp = DoubleListNode(value)
        if self._tail_node is None:
            temp.set_prev_node(temp)
            self._head_node = temp
        else:
            self._tail_node.set_prev_node(temp)
            temp.set_next_node(self._tail_node)
        self._tail_node = temp

    def size(self):
        if self._tail_node is not None and self._head_node is not None:
            current_node = self._tail_node
            count_node = 0
            while current_node is not None:
                count_node = count_node + 1
                current_node = current_node.get_next_node()
        else:
            count_node = 'Linked List is empty'
        return count_node

