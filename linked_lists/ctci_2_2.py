# Return Kth to Last: Implement an algorithm to find the kth to last element of a singly linked list.

# For this implementation we'll assume the linked list does NOT have a size attribute

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

def k_to_last_1(lst, k):
    size = lst_size(lst)
    target = size - k
    current_node = lst.head
    for _ in range(k):
        current_node = current_node.next
    return current_node.data


def lst_size(lst):
    current_node = lst.head
    size = 0
    while current_node != None:
        size += 1
        current_node = current_node.next
    
    return size

def k_to_last_2(lst, k):
    current_node = lst.head
    count = 0
    while current_node != None:
        if count < k:
            k_node = None
        
        if count == k:
            k_node = lst.head
        count += 1
        current_node = current_node.next
        if current_node == None and k_node != None:
            return k_node.data
        elif current_node == None and k_node == None:
            return None
        elif k_node:
            k_node = k_node.next
        
    return k_node.data
        

if __name__ == "__main__":
    # Build Linked List
    lst_1 = LinkedList()
    lst_2 = LinkedList()
    nums = [1, 2, 1, 3, 2, 4, 5, 1]
    for num in nums:
        lst_1.add(num)
        lst_2.add(num)

    print(k_to_last_1(lst_1, 1))    
    print(k_to_last_2(lst_1, 1))    