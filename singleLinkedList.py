from listNode import ListNode


class _SingleLinkedList:
    def __init__(self):
        self._head_node = None

    def get_head_node(self):
        return self._head_node

    def add(self, value):
        pass

    # Gskhgdlfkjghdak; fghsl kfjg hdflkj hsf;lg kd

    def find(self, node):
        if node is not self._head_node:
            current_node = self._head_node.get_next_node()
            while current_node is not None:
                if current_node is node:
                    return True
                elif current_node is self._head_node:
                    current_node = None
                else:
                    current_node = current_node.get_next_node()
        else:
            return True

    def size(self):
        if self._head_node is not None:
            current_node = self._head_node.get_next_node()
            count = 1
            while current_node is not None:
                if current_node is None or current_node is self._head_node:
                    current_node = None
                else:
                    count = count + 1
                    current_node = current_node.get_next_node()
        else:
            count = 0
        return count

    def delete_node(self, node):
        current_node = self._head_node
        if self.find(node):
            while current_node is not None:
                tail_node = current_node.get_next_node()
                if tail_node is node:
                    tail_node = tail_node.get_next_node()
                    current_node.set_next_node(tail_node)
                    return True
                else:
                    current_node = current_node.get_next_node()
        else:
            return False


class SingleWayList(_SingleLinkedList):
    def add(self, value):
        tmp_node = ListNode(value)
        if self._head_node is None:
            self._head_node = tmp_node
        else:
            tmp_node.set_next_node(self._head_node)
            self._head_node = tmp_node


class SingleWayLoopedList(_SingleLinkedList):
    def add(self, value):
        tmp_node = ListNode(value)
        if self._head_node is None:
            tmp_node.set_next_node(tmp_node)
            self._head_node = tmp_node
        else:
            tmp_node.set_next_node(self._head_node.get_next_node())
            self._head_node.set_next_node(tmp_node)
            self._head_node = tmp_node

