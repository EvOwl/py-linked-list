# -*- coding: utf-8 -*-
from listNode import ListNode


class LinkedLoopedList:
    def __init__(self):
        self._root_list = None

    def get_root_list(self):
        return self._root_list

    def add(self, value):
        tmp_node = ListNode(value)
        if self._root_list is None:
            tmp_node.set_next_node(tmp_node)
            self._root_list = tmp_node
        else:
            tmp_node.set_next_node(self._root_list.get_next_node())
            self._root_list.set_next_node(tmp_node)
            self._root_list = tmp_node

    def remove(self, node):
        current_node = self._root_list
        while current_node is not None:
            tail_node = current_node.get_next_node()
            if tail_node is node:
                tail_node = tail_node.get_next_node()
                return current_node.set_next_node(tail_node)
            else:
                current_node = current_node.get_next_node()

    def size(self):
        current_node = self._root_list.get_next_node()
        count = 1
        while current_node is not self._root_list:
            count = count + 1
            current_node = current_node.get_next_node()
        return count


L = LinkedLoopedList()
L.add('Node 0')
a = L.get_root_list()
L.add('Node 1')
L.add('Node 2')
L.add('Node 3')
L.add('Node 4')
print(L.size())
L.remove(a)
print(L.size())
print('Fin')
