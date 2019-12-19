# Binary Search Tree with AVL balancing 

class Node:
    '''Node properties for a node instance in the AVL BST'''
    # Access to properties will be performed directly, not through an access method.
    # I see no reason to create code when a simple access already exists. If i can 
    # find more information on proper implementation I will update accordingly.
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.height = 0

class BST:
    '''Binary Search Tree class contains methods to provide public functionality of 
        put, get, and delete. The integrety of the tree is maintained through AVL
        balancing methods'''
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, value):
        '''inserts key, value pair into the BST by ways of the _put helper function'''
        # Create new node:
        new_node = Node(key, value)

        # Case 1. The BST is empty. Create node and add it to the root property.
        if self.root == None:
            self.root = new_node
        
        # Case 2. The BST is not empty. Invoke the _put method to find the appropriate
        #   insertion point and insert the new node
        else:
            self._put(new_node, self.root)
        
        self.size += 1

    def _put(self, new_node, current_node):
        '''Recursively traverse BST to find insertion point for new node. Once found,
            as the recursive function unwinds, update the balance factor at each node.
            Note: if node keys are equal, the node will be a left child of the already
            placed node'''
        # Determine path:
        if new_node.key <= current_node.key:
            if current_node.left_child == None:
                new_node.parent = current_node
                current_node.left_child = new_node
            else:
                self._put(new_node, current_node.left_child)
        else:
            if current_node.right_child == None:
                new_node.parent = current_node
                current_node.right_child = new_node
            else:
                self._put(new_node, current_node.right_child)

        # Set balance factor on unwind:
        balance_factor = self.check_balance_factor(current_node)

        # Rebalance if neccessary:
        if balance_factor > 1:
            self.rebalance(current_node)

    def check_balance_factor(self, node):
        '''calculates and updates the balance factor of a node.'''
        # Calculate height and balance factor
        if node.left_child and node.right_child:
            node.height = 1 + max(node.left_child.height, node.right_child.height)
            balance_factor = abs(node.left_child.height - node.right_child.height)
        elif  node.left_child:
            node.height = 1 + node.left_child.height
            balance_factor = 1 + node.left_child.height
        elif node.right_child:
            node.right_child.height
            balance_factor = 1 + node.right_child.height
        else:
            balance_factor = 0
        
        return balance_factor

    def rebalance(self, node):
        pass

        

        

        

