from singleLinkedList import SingleWayList, SingleWayLoopedList
import numpy as np
import cv2


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


cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Video', frame)
    # cv2.imshow('frame',gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


