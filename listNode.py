# -*- coding: utf-8 -*-


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

