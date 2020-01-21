# Binary Search Tree with AVL balancing 
from collections import deque

# TODO:
#   -Add comments for methods from traverse down
#   -Make distributable package

class Node:
    """
    A class containing node properties for nodes in AVL BST.

    Attributes:
        Attributes required at instantiation:
            key (int): Unique key to access node.
            value (var): Value held in node, can be of any type.
        
        Attributes set as None at instantiation:
            left_child (node): A reference to the left child of the node.
            right_child (node): A reference to the right child of the node.
            parent (node): A reference to the parent if the node
            height (int): The height of the node
    """

    def __init__(self, key, value):
        """
        The constructor for Node class.

        Parameters:
            key (int): Unique key to access node.
            value (var): Value held in node, can be of any type.
        """

        self.key = key
        self.value = value
        self.left_child = None
        self.right_child = None
        self.parent = None
        self.height = 0

class BST:
    """
    A class containing methods to put, find and delete nodes in a binary search tree
    while maintaing a balance factor of less than or equal to 1

    Attributes:
        root (node): A reference to the root node of the AVL BST.
        size (int): A count of the number of items in thte AVL BST.

    Public Methods:
        put(key, value): Adds a node to the AVL BST.
        get(key): Retrieves a node in teh AVL BST.
        delete(key): Removes a node from the AVL BST. 
    """
    
    def __init__(self):
        """The constructor for the BST class."""
        self.root = None
        self.size = 0


    # ===================================================================================
    # ==================PUT METHODS TO INSERT A KEY, VALUE PAIR INTO BST=================

    def put(self, key, value):
        """
        Method to add key, value pair to AVL BST.

        Parameters:
            key (int): Unique key to access node.
            value (var): Value held in node, can be of any type. 
        """

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
        # Helper method to the public put method.
        #
        # Recursively traverses BST to find insertion point for new node based on key.
        # Updates node heights, checking balance factor and rebalancing on unwind.
        #
        # Note: If node keys are equal, the node will be a left child of the already 
        #       placed node.
        
        # Determine path
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
        self.update_node_height(current_node)
        
        if self.get_balance_factor(current_node) > 1:
            self.rebalance(current_node)

    
    # ===================================================================================
    # =================GET METHODS TO RETRIEVE A KEY, VALUE PAIR FROM BST================

    def get(self, key):
        """
        Method to retrieve node based on key.
        
        Parameters:
            key(int): Key value of node to be retrieved.
        
        Returns:
            Node object if found
            None if not found
        """

        if self.root:
            return self._get(key, self.root)
       
        return None
    
    def _get(self, key, current_node):
        # Private method to the public get method.
        #
        # Recursively traverses AVL BST looking for target key. Returns node if found.
        # 
        # Parameters:
        #   key(int): Key value of node to be retrieved.  
        #
        # Returns:
        #   Node object if found
        #   None if not found
        if current_node == None:
            return None
        elif current_node.key == key:
            return current_node
        elif current_node.key > key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)
    

    # ===================================================================================
    # ================DELETE METHODS TO REMOVE A KEY, VALUE PAIR FROM BST================

    def delete(self, key):
        """
        Method to delete node given key.

        Parameters:
            key(int): key value of node to be retrieved.

        Raises:
            KeyError: key not found.
        """
        # Dependencies:
        #   find_successor:
        #   rebalance_after_delete:
        #   splice:
        #   insert_successor

        node_to_remove = self._get(key, self.root)
        if node_to_remove is None:
            raise KeyError('Key not found in tree.')
        else:
            successor = self.find_successor(node_to_remove)
            
            # Case 1. Node is a leaf or single root
            if successor is None:
                if node_to_remove.parent:
                    if node_to_remove == node_to_remove.parent.left_child:
                        node_to_remove.parent.left_child = None

                        # Rebalance after deletion
                        self.rebalance_after_delete(node_to_remove.parent)    
                    else:
                        node_to_remove.parent.right_child = None
                else:
                    self.root = None
            
            # Case 2. Node has both children
            elif node_to_remove.left_child and node_to_remove.right_child:
                self.splice(successor)
                self.rebalance_after_delete(successor.parent)
                self.insert_successor(successor, node_to_remove)

            # Case 3. Node has only one child
            else:
                self.splice(node_to_remove)
            
                # Rebalance after deletion
                self.rebalance_after_delete(node_to_remove.parent)
            
            # Reduce the size of the tree
            self.size -= 1

    def find_successor(self, node):
        # Private method to find the right branch successor of any node in the AVL BST.
        #
        # The successor is the lowest valued key in the right branch of the node.
        #
        # Parameters:
        #   node(node): node object to find the successor of.
        # 
        # Returns:
        #   node(node): successor node.
        #
        # Dependencies:
        #   find_min:

        # Case 1 Node has no children       
        if not node.left_child and not node.right_child:         
            return None      

        # Case 2 Node has both children. The successor is the node
        #   with the minimum key value in the right sub-tree
        elif node.left_child and node.right_child:
            return self.find_min(node.right_child)        

        # Case 3 Node has only one child. The successor is the
        # child of the given node
        else:
            if node.left_child:
                return node.left_child
            else:
                return node.right_child

    def find_min(self, node):
        # Private method to find the node with the minimum key value in a branch.
        #
        # Parameters:
        #   node(node): node object local root of branch to search.
        #
        # Returns:
        #   node(node): node object of minimum node in branch.

        current_node = node
        while current_node.left_child:
            current_node = current_node.left_child            
        
        return current_node

    def splice(self, node):
        # Private method to splice node out of tree by removing all refrences to
        # and from the node.
        #
        # Parameters:
        #   node(node): node object to splice from AVL BST.
      
        # Case 1. node is a leaf.
        if not node.left_child and not node.right_child:
            if node == node.parent.left_child:
                node.parent.left_child = None
            else:
                node.parent.right_child = None

        # Case 2. node has child. 
        #   Note: successor node will never have a left child since the successor 
        #   node is the min key value in a sub-tree. But since splice is also used 
        #   to delete a node with only one child, the following code handles both children cases
        else:
            if node.left_child:
                if node == node.parent.left_child:
                    node.parent.left_child = node.left_child
                else:
                    node.parent.right_child = node.left_child
                
                # set left child's parent reference:
                node.left_child.parent = node.parent

            else:
                if node == node.parent.left_child:
                    node.parent.left_child = node.right_child
                else:
                    node.parent.right_child = node.right_child
                
                # set right child's parent reference:
                node.right_child.parent = node.parent
    
    def insert_successor(self, successor_node, deleted_node):
        # Private method to replace a node in AVL BST.
        #
        # Parameters:
        #   successor_node(node): node to be inserted.
        #   deleted_node(node): node to be replaced.
        
        # Set parent node references
        successor_node.parent = deleted_node.parent
        if deleted_node.parent:
            if deleted_node == deleted_node.parent.left_child:
                deleted_node.parent.left_child = successor_node
            else:
                deleted_node.parent.right_child = successor_node
        else:
            # If the deleted node has no parent it is the root. Set the new root
            self.root = successor_node

        # Set deleted_node's children's parent references to successor_node
        successor_node.left_child = deleted_node.left_child
        deleted_node.left_child.parent = successor_node

        successor_node.right_child = deleted_node.right_child
        deleted_node.right_child.parent = successor_node

    def __delitem__(self, key):
        self.delete(key) 
    
    
    # ===================================================================================
    # =======REBALANCE METHODS TO REBALANCE BST AFTER INSERT OR DELETION OF A NODE======= 
    
    def update_node_height(self, node):
        # Private method to update a single nodes height
        #
        # Parameters:
        #   node(node): node to calculate height of.
        
        if node.left_child and node.right_child:
            node.height = 1 + max(node.left_child.height, node.right_child.height)
        elif node.left_child:
            node.height = 1 + node.left_child.height
        elif node.right_child:
            node.height = 1 + node.right_child.height
        else:
            node.height = 0

    def update_parent_node_heights(self, node):
        # Private method to update nodes in a branch from the parameter node to the root.
        #
        # Parameters:
        #   node(node): node to start height update from.
        #
        # Dependencies:
        #   update_node_height

        while node != None:
            self.update_node_height(node)            
            node = node.parent
    
    def get_balance_factor(self, node):
        # Private method to calculate the balance factor at a given node
        #
        # Parameters:
        #   node(node): node to claculate balance factor for.
        #
        # Returns:
        #   balance_factor(int): calculated balance factor.

        if node.left_child and node.right_child:
            balance_factor = abs(node.left_child.height - node.right_child.height)        
        elif node.left_child:
            balance_factor = abs(node.left_child.height + 1)     
        elif node.right_child:
            balance_factor = abs(node.right_child.height + 1)    
        else:
            balance_factor = 0    
   
        return balance_factor


    def rebalance(self, node):
        # Private method to determine the rotation sequence to rebalance AVL BST.
        #
        # Parameters: 
        #   node(node): local root to rebalance 
        # 
        # Dependencies:
        #   right_rotation:
        #   left_rotation
        #   update_parent_node_heights:
        
        # Node has both children:
        if node.left_child and node.right_child:
            # Case 1. Left branch is heavy
            if node.left_child.height > node.right_child.height:
                # Node's left child has both children
                if node.left_child.left_child and node.left_child.right_child:
                    # Case 1a. Nodes left child is left heavy - right rotation about node
                    if node.left_child.left_child.height >= node.left_child.right_child.height:
                        self.right_rotation(node)

                    # Case 1b. Nodes left child is right heavy - Left rotation about left child,
                    #   followed by right rotation about node
                    else:
                        self.left_rotation(node.left_child)
                        self.right_rotation(node)

                # Node's left child has only left child
                # Case 1a. Nodes left child is left heavy - right rotation about node
                elif node.left_child.left_child:
                    self.right_rotation(node)

                # Node's left child only has right child
                # Case 1b. Nodes left child is right heavy - Left rotation about left child,
                #   followed by right rotation about node
                elif node.left_child.right_child:
                    self.left_rotation(node.left_child)
                    self.right_rotation(node)
            
            # Case 2. Right branch is heavy
            else:
                # Node's right child has both children
                if node.right_child.left_child and node.right_child.right_child:
                    # Case 2a. Nodes right child is right heavy - left rotation about node
                    if node.right_child.right_child.height > node.right_child.left_child.height:
                        self.left_rotation(node)

                    # Case 2b. Nodes right child is left heavy - Right rotation about right child,
                    #   followed by left rotation about node
                    else:
                        self.right_rotation(node.right_child)
                        self.left_rotation(node)
                
                # Node's right child has only right child
                # Case 2a. Nodes right child is right heavy - left rotation about node
                elif node.right_child.right_child:
                    self.left_rotation(node)

                # Node's right child has only left child
                # Case 2b. Nodes right child is left heavy - right rotation about right child,
                #   followed by left rotation about node
                elif node.right_child.left_child:
                    self.right_rotation(node.right_child)
                    self.left_rotation(node)
        
        # Node has only left child
        elif node.left_child:
            # Node's left child has both children
            if node.left_child.left_child and node.left_child.right_child:
                # Case 1a. Nodes left child is left heavy - right rotation about node
                if node.left_child.left_child.height >= node.left_child.right_child.height:
                    self.right_rotation(node)

                # Case 1b. Nodes left child is right heavy - Left rotation about left child,
                #   followed by right rotation about node
                else:
                    self.left_rotation(node.left_child)
                    self.right_rotation(node)

            # Node's left child has only left child
            # Case 1a. Nodes left child is left heavy - right rotation about node
            elif node.left_child.left_child:
                self.right_rotation(node)

            # Node's left child only has right child
            # Case 1b. Nodes left child is right heavy - Left rotation about left child,
            #   followed by right rotation about node
            elif node.left_child.right_child:
                self.left_rotation(node.left_child)
                self.right_rotation(node)

        # Node has only right child
        else:
            # Node's right child has both children
            if node.right_child.left_child and node.right_child.right_child:
                # Case 2a. Nodes right child is right heavy - left rotation about node
                if node.right_child.right_child.height > node.right_child.left_child.height:
                    self.left_rotation(node)

                # Case 2b. Nodes right child is left heavy - Right rotation about right child,
                #   followed by left rotation about node
                else:
                    self.right_rotation(node.right_child)
                    self.left_rotation(node)
            
            # Node's right child has only right child
            # Case 2a. Nodes right child is right heavy - left rotation about node
            elif node.right_child.right_child:
                self.left_rotation(node)

            # Node's right child has only left child
            # Case 2b. Nodes right child is left heavy - right rotation about right child,
            #   followed by left rotation about node
            elif node.right_child.left_child:
                self.right_rotation(node.right_child)
                self.left_rotation(node)

        # Update parent heights
        self.update_parent_node_heights(node)

    def left_rotation(self, node):
        # Private method to perform left roationa about root node
        #
        # Parameters:
        #   node(node): node to perform rotation about
        #
        # Dependencies:
        #   update_node_height:
        
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
            new_root.parent = None
        
        # link new_root's left_child to node's right child
        if new_root.left_child:
            node.right_child = new_root.left_child
            node.right_child.parent = node
        else:
            node.right_child = None

        
        # Set new_roots left child to node
        new_root.left_child = node
        node.parent = new_root

        # Update heights
        self.update_node_height(node)
        self.update_node_height(new_root)
        
        
    def right_rotation(self, node):
        # Private method to perform right roationa about root node
        #
        # Parameters:
        #   node(node): node to perform rotation about
        #
        # Dependencies:
        #   update_node_height:

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
            new_root.parent = None
        
        # link new_root's right_child to node's left child
        if new_root.right_child:
            node.left_child = new_root.right_child
            node.left_child.parent = node
        else:
            node.left_child = None
        
        # Set new_roots right child to node
        new_root.right_child = node
        node.parent = new_root

        # Update heights
        self.update_node_height(node)
        self.update_node_height(new_root)


    def rebalance_after_delete(self, node):
        # Private method to check and trigger rebalance tree after a node is deleted
        #
        # Evaluates height and evaluates balance factor at each node as it climbs from
        # starting paramater node.
        #
        # Parameters:
        #   node(node): starting node for rebalance evaluation.
        #
        # Dependencies:
        #   update_node_height:
        #   get_balance_factor:
        #   rebalance

        while node:
            self.update_node_height(node)
            if self.get_balance_factor(node) > 1:
                node_parent = node.parent
                self.rebalance(node)
                node = node_parent
            else:
                node = node.parent

    # ===================================================================================
    # =================================TRAVERSAL METHODS=================================       
    
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

    def pre_order_traversal(self):
        map = {}
        self._pre_order_traversal(self.root, map)
        return map

    def _pre_order_traversal(self, node, map):
        if node:
            map[node] = {'left': node.left_child, 'right': node.right_child}
            self._pre_order_traversal(node.left_child, map)
            self._pre_order_traversal(node.right_child, map)

    def in_order_traversal(self):
        map = {}
        self._in_order_traversal(self.root, map)
        return map

    def _in_order_traversal(self, node, map):
        if node:
            self._in_order_traversal(node.left_child, map)
            map[node] = {'left': node.left_child, 'right': node.right_child}
            self._in_order_traversal(node.right_child, map)

    def post_order_traversal(self):
        map = {}
        self._post_order_traversal(self.root, map)
        return map

    def _post_order_traversal(self, node, map):
        if node:
            self._post_order_traversal(node.left_child, map)
            self._post_order_traversal(node.right_child, map)
            map[node] = {'left': node.left_child, 'right': node.right_child}


    

        

        

        

