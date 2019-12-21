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
        self.balance_factor = 0

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
        #if current_node is None:
        #    print("NONE")
        #balance_factor = self.update_balance_factor(current_node)

        # Rebalance if neccessary:
        #if balance_factor > 1:
        #    self.rebalance(current_node)

    def update_balance_factor(self, node):
        if node.left_child and node.right_child:
            node.balance_factor = abs(node.left_child.balance_factor - node.right_child.balance_factor)        
        
        elif node.left_child:
            node.balance_factor = abs(node.left_child.balance_factor - -1)     

        elif node.right_child:
            node.balance_factor = abs(-1 - node.right_child.balance_factor)        
   
        return node.balance_factor

    def rebalance(self, node):
        '''Rebalance the tree'''
        # Case 1. Left branch is heavy.
        if node.left_child.height > node.right_child.height:
            # Case 1a. Nodes left child is left heavy - right rotation about node
            if node.left_child.left_child.height >= node.left_child.right_child.height:
                self.right_rotation(node)

            # Case 1b. Nodes left child is right heacy - Left rotation about left child,
            #   followed by right rotation about node
            else:
                self.left_rotation(node.left_child)
                self.right_rotation(node)
        
        # Case 2. Right branch is heavy
        else:
            # Case 2a. Nodes right child is right heavy - left rotation about node
            if node.right_child.right_child.height >= node.right_child.left_child.height:
                self.left_rotation(node)
            
            # Case 2b. Nodes right child is left heavy - right rotation about right child,
            #   followed by left rotation about node
            else:
                self.right_rotation(node.right_child)
                self.left_rotation(node)

    def left_rotation(self, node):
        pass

    def right_rotation(self, node):
        pass
        

        

        

