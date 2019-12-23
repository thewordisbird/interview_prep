# Binary Search Tree with AVL balancing 
from collections import deque

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
        #self.balance_factor = 0

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
        
        # Update height and check balance factor on unwind
        self.update_height(current_node)
        if self.get_balance_factor(current_node) > 1:
            self.rebalance(current_node)

        # Set balance factor on unwind:
        #if current_node is None:
        #    print("NONE")
        #balance_factor = self.update_balance_factor(current_node)

        # Rebalance if neccessary:
        #if balance_factor > 1:
        #    self.rebalance(current_node)

    def update_height(self, node):
        
        if node.left_child and node.right_child:
            #print(node.left_child.height, node.right_child.height)
            node.height = 1 + max(node.left_child.height, node.right_child.height)
        elif node.left_child:
            node.height = 1 + node.left_child.height
        elif node.right_child:
            node.height = 1 + node.right_child.height

    def get_balance_factor(self, node):
        if node.left_child and node.right_child:
            balance_factor = abs(node.left_child.height - node.right_child.height)        
        elif node.left_child:
            balance_factor = abs(node.left_child.height - -1)     
        elif node.right_child:
            balance_factor = abs(-1 - node.right_child.height)        
   
        return balance_factor

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
        new_root = node.right_child
        # Set new_roots' parent to node's parent
        if node.parent:
            new_root.parent = node.parent
            if node.parent.left_child == node:
                node.parent.left_child = new_root
            else:
                node.parent.right_child = new_root
        else:
            self.root = new_root
            new_root.pair = None
        
        # link new_root's left_child to node's right child
        if new_root.left_child:
            node.right_child = new_root.left_child
            node.right_child.parent = node
        
        # Set new_roots left child to node
        new_root.left_child = node
        node.parent = new_root

        # Update heights
        if node.left_child:
            node.height = 1 + max(node.left_child.height, node.right_child.height)
        else:
            node.height = 1 + node.right_child.height

        new_root.height = 1 + max(new_root.left_child.height, new_root.right_child.height)

    def right_rotation(self, node):
        new_root = node.left_child
        # Set new_roots' parent to node's parent
        if node.parent:
            new_root.parent = node.parent
            if node.parent.left_child == node:
                node.parent.left_child = new_root
            else:
                node.parent.right_child = new_root
        else:
            self.root = new_root
            new_root.pair = None
        
        # link new_root's right_child to node's left child
        if new_root.right_child:
            node.left_child = new_root.right_child
            node.left_child.parent = node
        
        # Set new_roots right child to node
        new_root.right_child = node
        node.parent = new_root

        # Update heights
        if node.right_child:
            node.height = 1 + max(node.left_child.height, node.right_child.height)
        else:
            node.height = 1 + node.right_child.height

        new_root.height = 1 + max(new_root.left_child.height, new_root.right_child.height)

    def breadth_first_traversal(self):
        nodes = []
        q = deque()
        q.append(self.root)
        
        while q:
            current_node = q.popleft()
            if current_node.left_child:
                q.append(current_node.left_child)
            if current_node.right_child:
                q.append(current_node.right_child)
            
            #print(f'Key: {current_node.key}, Value: {current_node.value}')
            nodes.append(current_node.value)

        return nodes

    

        

        

        

