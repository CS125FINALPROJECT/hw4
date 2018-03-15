"""
Homework 4 - Linked Lists

To understand recursion, you must first understand recursion.
"""

class Node:
    """
    Class for linked list node.
    """
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

def list_length(head):
        count = 0
        runner = head
        while runner:
            count += 1
            runner = head.next
        return count

    # Given a linked list, returns the length ofthe linked list.
    # Suppose the existing linked list looks like this: 3 -> 5 -> 9 -> 6
    # Then the length is 4.
    #
    # Input:
    #     head - the head Node of a linked list
    #
    # Returns:
    #     (int) The length of the linked list


def add_head(head, data):
    node = Node(data)
    if head == None:
        head = node
    else:
        node.next_node = head
        head = node
    return head

    # """
    # Prepends a new Node to a linked list. You are given the head
    # of the linked list and the data for the new Node.
    #
    # Example:
    # Suppose the existing linked list looks like this: 3 -> 5 -> 9 -> 6
    # In this case, head is a Node with head.data = 3. If the data argument
    # is 10, then the resulting linked list should look like this:
    # 10 -> 3 -> 5 -> 9 -> 6
    #
    # Input:
    #     head - the head Node of a linked list
    #     data - the data element you'll need to add to the list
    #
    # Returns:
    #     (Node) the head of the new linked list that includes 'data'
    # """



def add_tail(head, data):
    node = Node(data)
    runner = head
    while runner != None:
        runner = runner.next_node

    runner = node
    return head
#         """
#     Appends a new Node to a linked list. You are given the head of
#     the linked list and the data for the new Node.
#
#     Example:
#     Suppose the existing linked list looks like this: 7 -> 8 -> 2
#     In this case, head is a Node with head.data = 7. If the data argument
#     is 4, then the resulting linked list should look like this:
#     7 -> 8 -> 2 -> 4
#
#     Input:
#         head - the head Node of a linked list
#         data - the data element you'll need to add to the list
#
#     Returns:
#         (Node) the head of the new linked list that includes 'data'
#     """
# pass


def remove_position(head, position):
        """
    Given the head of a linked list, removes the element of the 
    specified position. If the position is greater than the length
    of the linked list, do not remove anything.

    Input:
        head - the head of the linked list.
        position - the position at which to remove an element.
    
    Output:
        the head of the linked list.
    """
pass


def find_cycle(head):
        """
    Given the head of a linked list, determines whether or not there
    is a cycle in the linked list.
    
    Ex. suppose we have a linked list 3 -> 4 -> 7, and the last node points
    back to the node labeled 4. Then this linked list has a cycle.
    
    Input:
        head - the head of the linked list.
    
    Output:
        (bool) whether or not there is a cycle in the linked list.
    """
pass
