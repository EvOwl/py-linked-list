# -*- coding: utf-8 -*-
from listNode import ListNode


class SingleLinkedList:
    def __init__(self):
        self._head_list = None

    def add(self, value):
        tmp_node = ListNode(value)
        if self._head_list is None:
            self._head_list = tmp_node
        else:
            tmp_node.set_next_node(self._head_list)
            self._head_list = tmp_node

    def remove(self, node):
        current_node = self._head_list
        while current_node is not None:
            tail_node = current_node.get_next_node()
            if tail_node is node:
                tail_node = tail_node.get_next_node()
                return current_node.set_next_node(tail_node)
            else:
                current_node = current_node.get_next_node()

    def get_head_list(self):
        return self._head_list

    def size(self):
        current_node = self._head_list
        count = 0
        while current_node is not None:
            count = count + 1
            current_node = current_node.get_next_node()
        return count


# Testing Code:
L = SingleLinkedList()
L.add('Node 0')
L.add('Node 1')
L.add('Node 2')
a = L.get_head_list()
L.add('Node 3')
L.add('Node 4')
print(L.size())
L.remove(a)
print(L.size())
