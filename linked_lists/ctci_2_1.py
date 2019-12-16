# Remove Dups: Write code to remove duplicates from an unsorted linked list.

# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.size += 1

    def __repr__(self):
        lst_str = ""
        current_node = self.head
        while current_node.next != None:
            lst_str = lst_str + f'{current_node.data} -> '
            current_node = current_node.next
        lst_str = lst_str + f'{current_node.data}'
        return lst_str

def delete_dups_buffer(lst):
    seen_values = set()
    current_node = lst.head
    previous_node = None
    while current_node != None:
        if current_node.data not in seen_values:
            seen_values.add(current_node.data)
        else:
            delete_node(lst, current_node, previous_node)
            current_node = previous_node
        previous_node = current_node
        current_node = current_node.next

def delete_node(linked_list, node, previous_node):
    previous_node.next = node.next
    node.next = None
    linked_list.size -= 1

def delete_dups_no_buffer(lst):
    pointer_slow = lst.head
    while pointer_slow != None:
        pointer_fast = pointer_slow.next
        previous_node = None
        while pointer_fast != None:
            if pointer_fast.data == pointer_slow.data:
                delete_node(lst, pointer_fast, previous_node)
                pointer_fast = previous_node
            previous_node = pointer_fast
            pointer_fast = pointer_fast.next

if __name__ == "__main__":

    # Build Linked List
    lst_1 = LinkedList()
    lst_2 = LinkedList()
    nums = [1, 2, 1, 3, 2, 4, 5, 1]
    for num in nums:
        lst_1.add(num)
        lst_2.add(num)

    print(lst_1.size)
    print(lst_1)
    delete_dups_buffer(lst_1)
    print(lst_1.size)
    print(lst_1)

    print(lst_2.size)
    print(lst_2)
    delete_dups_buffer(lst_2)
    print(lst_2.size)
    print(lst_2)