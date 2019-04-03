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


# Test block
L = SingleLinkedList()
L.add('Node 0')
L.add('Node 1')
L.add('Node 2')
iUseThisNode = L.get_head_list()
L.add('Node 3')
L.add('Node 4')
L.remove(iUseThisNode)
print(L.size())
