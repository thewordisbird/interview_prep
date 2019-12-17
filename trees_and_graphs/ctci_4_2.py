# Minimal Tree: Given a sorted (increasing order) array with unique integer
# elements, write an algorithm to create a binary search tree w/ minimal height
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def add(self, value):
        new_node = Node(value)
        if self.root == None:
            print(f'Adding {new_node.value} as root')
            self.root = new_node

        else:
            current_node = self.root
            while current_node != None:
                if new_node.value < current_node.value:
                    if current_node.left == None:
                        print(f'Adding {new_node.value} as left child of {current_node.value}')
                        current_node.left = new_node
                        break
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right == None:
                        print(f'Adding {new_node.value} as right child of {current_node.value}')
                        current_node.right = new_node
                        break
                    else:
                        current_node = current_node.right
                    

def minimal_tree(arr):
    bst = BST()
    arr_to_tree(bst, arr, 0, len(arr) - 1)

def arr_to_tree(bst, arr, min, max):
    if min <= max:
        mid = (max + min) // 2
        #print(min, max, mid)
        bst.add(arr[mid])

        # Pointers are off by one i think. maybe have max as non inclusive??
        arr_to_tree(bst, arr, min, mid - 1)
        arr_to_tree(bst, arr, mid + 1, max)


if __name__ == "__main__":
    arr = [1, 3, 4, 7, 10, 12, 16, 25]
    minimal_tree(arr)