class ListNode:
    def __init__(self, value=None, next_node=None, previous_node=None):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node

    def get_value(self):
        return self.value

    def get_next_node(self):
        return self.next_node

    def get_previous_node(self):
        return self.next_node

    def set_previous_node(self, new_previous_node):
        self.previous_node = new_previous_node

    def set_value(self, new_value):
        self.value = new_value

    def set_next_node(self, new_next_node):
        self.next_node = new_next_node


class LinkedList:
    def __init__(self):
        self.head_list = None
        self.tail_list = None

    def add_node_head(self, value):
        temp = ListNode(value)
        if self.head_list is None:
            temp.set_next_node(temp)
            self.tail_list = temp
        else:
            self.head_list.set_next_node(temp)
            temp.set_previous_node(self.head_list)
        self.head_list = temp

    def add_node_tail(self, value):
        temp = ListNode(value)
        if self.tail_list is None:
            temp.set_previous_node(temp)
            self.head_list = temp
        else:
            self.tail_list.set_previous_node(temp)
            temp.set_next_node(self.tail_list)
        self.tail_list = temp

    def size(self):
        if self.tail_list is not None and self.head_list is not None:
            current_node = self.tail_list
            count_node = 0
            while current_node is not None:
                count_node = count_node + 1
                current_node = current_node.get_next_node()
        else:
            return "Linked List is empty"

        return count_node


L = LinkedList()

L.add_node_head(10001)
L.add_node_tail(44440)
L.add_node_head(20002)
L.add_node_tail(55550)
L.add_node_head(30003)
L.add_node_tail(66660)

print(L.size())
print('fin')