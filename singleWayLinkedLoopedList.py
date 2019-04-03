# -*- coding: utf-8 -*-
from listNode import ListNode


class LinkedLoopedList:
    def __init__(self):
        self._root_node = None

    def get_root_list(self):
        return self._root_node

    def add(self, value):
        tmp_node = ListNode(value)
        if self._root_node is None:
            tmp_node.set_next_node(tmp_node)
            self._root_node = tmp_node
        else:
            tmp_node.set_next_node(self._root_node.get_next_node())
            self._root_node.set_next_node(tmp_node)
            self._root_node = tmp_node

    def remove(self, node):
        current_node = self._root_node
        while current_node is not None:
            tail_node = current_node.get_next_node()
            if tail_node is node:
                tail_node = tail_node.get_next_node()
                return current_node.set_next_node(tail_node)
            else:
                current_node = current_node.get_next_node()

    def size(self):
        if self._root_node is not None:
            current_node = self._root_node.get_next_node()
            count = 1
            while current_node is not self._root_node:
                count = count + 1
                current_node = current_node.get_next_node()
        else:
            count = 'Linked List is empty'
        return count

