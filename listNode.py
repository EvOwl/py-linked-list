# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, value=None, next_node=None, prev_node=None):
        self._value = value
        self._next_node = next_node
        self._prev_node = prev_node

    def get_value(self):
        return self._value

    def get_next_node(self):
        return self._next_node

    def get_prev_node(self):
        return self._prev_node

    def set_value(self, new_value):
        self._value = new_value

    def set_next_node(self, new_next_node):
        self._next_node = new_next_node

    def set_prev_node(self, new_prev_node):
        self._prev_node = new_prev_node
