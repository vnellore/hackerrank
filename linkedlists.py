class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node


def has_cycle(head):
    visited_nodes = list()

    valid = False
    if head.next is None:
        return valid
    else:
        while valid is False and head.next is not None:
            if head in visited_nodes:
                valid = True
            else:
                visited_nodes.append(head)
                head = head.next

    return valid


def print_linked_list(head):
    if head.next is None:
        print(f'-->[{head.data}]')
    else:
        print(f'-->[{head.data}]')
        print_linked_list(head.next)
