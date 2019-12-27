class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_item(self, item):
        new_node = Node(item)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def print_reveresed(self):
        self._print_reveresed(self.head)

    def _print_reveresed(self, node):
        if node.next:
            # Recurse to end:
            self._print_reveresed(node.next)

            # Process on unwind
            print(node.value)
        else:
            print(node.value)
    def repr_reversed(self):
        print(self._repr_reversed(self.head))

    def _repr_reversed(self, node):
        if node.next:
            # To print in reverse:
            return self._repr_reversed(node.next) + ' -> ' + node.value
            
            # To print forward:
            #return  node.value + ' -> ' + self._repr_reversed(node.next)

        else:
            return node.value

if __name__ == "__main__":
    nodes = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    
    linked_list = LinkedList()
    # Because a linked list adds to the head the linked list becomes:
    # g -> f -> e -> d -> c -> b- > a
    for node in nodes:
        linked_list.add_item(node)

    linked_list.print_reveresed()
    # a
    # b
    # c
    # d
    # e
    # f
    # g

    linked_list.repr_reversed()
    # a -> b -> c -> d -> e -> f -> g