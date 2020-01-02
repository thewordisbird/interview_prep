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
        #print(f'Comparing {new_node.key} to {current_node.key}')
        if new_node.key <= current_node.key:
            if current_node.left_child == None:
                new_node.parent = current_node
                current_node.left_child = new_node
                print(f'Adding {new_node.key} as left child of {current_node.key}')
            else:
                
                self._put(new_node, current_node.left_child)
        else:
            if current_node.right_child == None:
                new_node.parent = current_node
                current_node.right_child = new_node
                print(f'Adding {new_node.key} as right child of {current_node.key}')
            else:
                self._put(new_node, current_node.right_child)
        
        # Update height and check balance factor on unwind
        self.update_height(current_node)
        #print(f'BF({current_node.key}) = {self.get_balance_factor(current_node)}')
        if self.get_balance_factor(current_node) > 1:
            print(f'rebalancing Key: {current_node.key}, Value: {current_node.value}')
            self.rebalance(current_node)


    def update_height(self, node):
        while node != None:
            if node.left_child and node.right_child:
                node.height = 1 + max(node.left_child.height, node.right_child.height)
            elif node.left_child:
                node.height = 1 + node.left_child.height
            elif node.right_child:
                node.height = 1 + node.right_child.height
            else:
                node.height = 0
            
            node = node.parent
        

    def get_balance_factor(self, node):
        if node.left_child and node.right_child:
            balance_factor = abs(node.left_child.height - node.right_child.height)        
        elif node.left_child:
            balance_factor = abs(node.left_child.height + 1)     
        elif node.right_child:
            balance_factor = abs(node.right_child.height + 1)        
   
        return balance_factor


    def rebalance(self, node):
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
        self.update_parent_heights(node)

    def update_parent_heights(self, node):
        pass
        
        

    def left_rotation(self, node):
        new_root = node.right_child
        print(f'left rotation about {node.key}')
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
        if node.right_child and node.left_child:
            node.height = 1 + max(node.left_child.height, node.right_child.height)
        elif node.right_child:
            node.height = 1 + node.right_child.height
        elif node.left_child:
            node.height = 1 + node.left_child.height
        else:
            node.height = 0

        if new_root.left_child and new_root.right_child:
            new_root.height = 1 + max(new_root.left_child.height, new_root.right_child.height)
        elif new_root.left_child:
            new_root.height = 1 + new_root.left_child.height
        elif new_root.right_child:
            new_root.height = 1 + new_root.right_child.height
        




    def right_rotation(self, node):
        new_root = node.left_child
        print(f'right rotation about {node.key}')
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
        if node.right_child and node.left_child:
            node.height = 1 + max(node.left_child.height, node.right_child.height)
        elif node.right_child:
            node.height = 1 + node.right_child.height
        elif node.left_child:
            node.height = 1 + node.left_child.height
        else:
            node.height = 0

        if new_root.left_child and new_root.right_child:
            new_root.height = 1 + max(new_root.left_child.height, new_root.right_child.height)
        elif new_root.left_child:
            new_root.height = 1 + new_root.left_child.height
        elif new_root.right_child:
            new_root.height = 1 + new_root.right_child.height


    def get(self, target_key):
        '''Find node by key and return value'''
        if self.root:
            result_node = self._get(target_key, self.root)
            if result_node:
                return result_node
            else:
                return None
        else:
            return None
    
    # NEEDS TESTING BELOW

    def _get(self, target_key, current_node):
        if current_node == None:
            return None
        elif current_node.key == target_key:
            return current_node
        elif current_node.key > target_key:
            return self._get(target_key, current_node.left_child)
        else:
            return self._get(target_key, current_node.right_child)

    def delete(self, key):
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
                    else:
                        node_to_remove.parent.right_child = None
                    
                    # Rebalance after deletion
                    self.rebalance_after_delete(parent)
                else:
                    self.root = None
            
            # Case 2. Node has both children
            elif node_to_remove.left_child and node_to_remove.right_child:
                self.splice(successor)
                # Rebalance after deletion
                self.rebalance_after_delete(parent)
                self.insert_successor(successor, node_to_remove)

            # Case 3. Node has only one child
            else:
                self.splice(node_to_remove)
                # Rebalance after deletion
                self.rebalance_after_delete(parent)

            self.size -= 1

    def find_successor(self, node):
        '''Finds and returns the appropriate successor node depending
            on the position of the node being deleted''' 
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
        '''Returns the minimum node in a subtree rooted with the 
            instance node'''
        current_node = node
        while current_node.left_child:
            print(f'visiting {current_node.key}')
            current_node = current_node.left_child
            
        return current_node

    def splice(self, node):
        '''Removes all refrences to the successor node and re-directs 
            relatives to the appropriate node'''
        # Case 1. node is a leaf.
        if not node.left_child and not node.right_child:
            if node == node.parent.left_child:
                node.parent.left_child = None
            else:
                node.parent.right_child = None

        # Case 2. node has child. Note: successor node will
        #   never have a left child since the successor node is the min key
        #   value in a sub-tree. But since splice is also used to delete a node
        #   with only one child, the following code handles both children cases
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

    
    def rebalance_after_delete(self, node):
        while node:
            self.update_height(node)
            if self.get_balance_factor > 1:
                self.rebalance(node)
            node = node.parent
                
    def insert_successor(self, successor_node, deleted_node):
        '''replaces the successor node pointers with those of the deleted node.
            in effect de-refrenceing the deleted node and inserting the successor
            node in its place. This is only used in when the deleted node has
            both children'''
        # Case 2. deleted_node has both children
        # Set parent node references
        successor_node.parent = deleted_node.parent
        if deleted_node == deleted_node.parent.left_child:
            deleted_node.parent.left_child = successor_node
        else:
            deleted_node.parent.right_child = successor_node
        
        # Set deleted_node's children's parent references to successor_node
        successor_node.left_child = deleted_node.left_child
        deleted_node.left_child.parent = successor_node

        successor_node.right_child = deleted_node.right_child
        deleted_node.right_child.parent = successor_node

    def __delitem__(self, key):
        self.delete(key) 


    # NEEDS TESTING ABOVE
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
    

        

        

        

