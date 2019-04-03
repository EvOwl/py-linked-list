# -*- coding: utf-8 -*-
from listNode import ListNode


class SingleLinkedList:
    def __init__(self):
        self._head_node = None

    def add(self, value):
        tmp_node = ListNode(value)
        if self._head_node is None:
            self._head_node = tmp_node
        else:
            tmp_node.set_next_node(self._head_node)
            self._head_node = tmp_node

    def remove(self, node):
        current_node = self._head_node
        while current_node is not None:
            tail_node = current_node.get_next_node()
            if tail_node is node:
                tail_node = tail_node.get_next_node()
                return current_node.set_next_node(tail_node)
            else:
                current_node = current_node.get_next_node()

    def get_head_list(self):
        return self._head_node

    def size(self):
        if self._head_node is not None:
            current_node = self._head_node
            count = 0
            while current_node is not None:
                count = count + 1
                current_node = current_node.get_next_node()
        else:
            count = 'Linked List is empty'
        return count

