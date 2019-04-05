from singleLinkedList import SingleWayList, SingleWayLoopedList

example_data = ['node0', 'node1', 'node2', 'node3', 'node4', 'node5']


def check_function(obj):
    for el in example_data:
        if el is 'node3':
            node_to_del = obj.get_head_node()
        obj.add(el)

    print('Size before del:', obj.size())
    obj.delete_node(node_to_del)
    print('Size after del:', obj.size())


print('Test Single Way List:')
check_function(SingleWayList())
print('Testing Single Way Looped List')
check_function(SingleWayLoopedList())
print('Done')
