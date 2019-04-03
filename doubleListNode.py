# -*- codig: utf-8 -*-
from listNode import ListNode


class DoubleListNode(ListNode):
    def __init__(self, value=None, next_node=None, prev_node=None):
        self._value = value
        self._next_node = next_node
        self._prev_node = prev_node

    def get_prev_node(self):
        return self._prev_node

    def set_prev_node(self, node):
        self._prev_node = node

