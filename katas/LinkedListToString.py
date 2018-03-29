
class Node():
    def __init__(self, data, next = None):
        self.data = data
        self.next = next


def stringify(node):
    data = []
    while node:
        data.append(str(node.data))
        node = node.next
    data.append('None')
    return ' -> '.join(data)


def stringify2(list):
    return 'None' if list == None else str(list.data) + ' -> ' + stringify(list.next)


print(stringify2(Node(0, Node(1, Node(4, Node(9, Node(16)))))))