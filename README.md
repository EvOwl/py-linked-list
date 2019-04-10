# Python Linked List

Example of single and double way linked list in Python 3+

Tasks:
- [X] Create single way linked list
- [X] Create single way linked looped list
- [X] Create double way linked list
- [ ] Create double way linked looped list

### Structure of Single way linked List:

node0 | node1 | node2 | node3 | <= | nodeN
------|-------|-------|-------|----|------
value: value | value: value | value: value | value: value | ... | value: value
next_node: None | next_node: node0 | next_node: node1 | next_node: node2 | ... | next_node: node3

### Structure of Single way lined List (looped):

node0 | node1 | node2 | node3 | <= | nodeN
------|-------|-------|-------|----|------
value: value | value: value | value: value | value: value | ... | value: value
next_node: nodeN | next_node: node0 | next_node: node1 | next_node: node2 | ... | next_node: node3

### Structure of Double way linked list:

node0 | node1 | node2 | node3 | <=> | nodeN
------|-------|-------|-------|----|------
value: value | value: value | value: value | value: value | ... | value: value
next_node: None | next_node: node0 | next_node: node1 | next_node: node2 | ... | next_node: node3
prev_node: node1 | prev_node: node2 | prev_node: node3 | prev_node: nodeN | ... | prev_node: None

### Structure of Double way linked list (looped):

node0 | node1 | node2 | node3 | <=> | nodeN
------|-------|-------|-------|----|------
value: value | value: value | value: value | value: value | ... | value: value
next_node: nodeN | next_node: node0 | next_node: node1 | next_node: node2 | ... | next_node: node3
prev_node: node1 | prev_node: node2 | prev_node: node3 | prev_node: nodeN | ... | prev_node: node0
