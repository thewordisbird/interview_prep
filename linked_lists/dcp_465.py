# Given the head of a singly linked list, reverse it inplace
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

class LinkedList:
    def __init__(self, head=None):
        self.head = head

def reverse_linked_list(linked_list):

    node = linked_list.head
    previous = [None]
    while node.next != None:
        #print(node.value)
        previous.append(node)
        node = node.next

    l.head = node
    # Reverse Linked List in place
    while previous:
        node.next = previous.pop()
        node = node.next

def print_ll(linked_list):
    print('printing')
    node = linked_list.head
    while node:
        print (node.value)
        node = node.next
        
if __name__ == "__main__":
    nodes = []
    for i in range(5, -1, -1):
        if i == 5:
            node = Node(i)
            nodes.append(node)
        else:
            node = Node(i, nodes[-1])
            print(nodes[-1].value)
            nodes.append(node)
            
    l = LinkedList(node)
    
    print_ll(l)

    reverse_linked_list(l)

    print_ll(l)