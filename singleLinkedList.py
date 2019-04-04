from listNode import ListNode


class SingleLinkedList:
    def __init__(self):
        self._head_node = None
        self._count_nodes = 0

    def get_head_node(self):
        return self._head_node

    def size(self):
        return self._count_nodes

    def add(self, value):
        pass

    def delete_node(self, node):
        current_node = self._head_node
        # AHTUNG!!!
        # If I inject NODE in not this Linked List this is crashed this code
        while current_node is not None:
            tail_node = current_node.get_next_node()
            if tail_node is node:
                tail_node = tail_node.get_next_node()
                self._count_nodes = self._count_nodes - 1
                return current_node.set_next_node(tail_node)
            else:
                current_node = current_node.get_next_node()


class SingleWayList(SingleLinkedList):
    def add(self, value):
        tmp_node = ListNode(value)
        if self._head_node is None:
            self._head_node = tmp_node
        else:
            tmp_node.set_next_node(self._head_node)
            self._head_node = tmp_node
        self._count_nodes = self._count_nodes + 1


class SingleWayLoopedList(SingleLinkedList):
    def add(self, value):
        tmp_node = ListNode(value)
        if self._head_node is None:
            tmp_node.set_next_node(tmp_node)
            self._head_node = tmp_node
        else:
            tmp_node.set_next_node(self._head_node.get_next_node())
            self._head_node.set_next_node(tmp_node)
            self._head_node = tmp_node
        self._count_nodes = self._count_nodes + 1

