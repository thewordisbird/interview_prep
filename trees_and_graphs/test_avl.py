import pytest

from avl import Node, BST
# Tests of methods in avl.py. Supporting both the Node and BST classes.

# Tests for Node Class
def test_node_construction():
    n = Node('key', 'value')
    assert n.key == 'key'
    assert n.value == 'value'
    assert n.left_child == None 
    assert n.right_child == None
    assert n.parent == None
    #assert n.height == 0




# Tests for BST Class
@pytest.fixture(scope='class')
def empty_bst():
    return BST()

@pytest.fixture(scope='class')
def rooted_bst():
    bst = BST()
    bst.put(6, 'A')
    return bst
    
def test_bst_construction():
    bst = BST()
    assert bst.root == None
    assert bst.size == 0

class TestPut:

    @pytest.mark.parametrize('new_node, parent, root_height', 
                                [
                                    (Node(3, 'B'), 'A', 1),
                                    (Node(9, 'C'), 'A', 1),
                                    (Node(2, 'D'), 'B', 2),
                                    (Node(4, 'E'), 'B', 2),
                                    (Node(10, 'F'), 'C', 2)
                                ])
    def test__put(self, rooted_bst, new_node, parent, root_height):
        bst = rooted_bst
        bst._put(new_node, bst.root)
        assert new_node.parent.value == parent
        assert rooted_bst.root.height == root_height

    def test_put_root(self, empty_bst):
        assert empty_bst.root == None
        assert empty_bst.size == 0
        empty_bst.put(6, 'val')
        assert empty_bst.root != None
        assert empty_bst.size == 1

    @pytest.mark.parametrize('key, value, size', 
                                [
                                    (3, 'B', 2),
                                    (9, 'C', 3),
                                    (2, 'D', 4),
                                    (4, 'E', 5)
                                ])
    def test_put(self, empty_bst, key, value, size):
        empty_bst.put(key, value)
        assert empty_bst.size == size

class TestBalance:
    right_heavy_right_child_right_heavy_bst = [
                (64, 'A', 4), (32, 'B', 1), (96, 'C', 3), (16, 'D', 0), (48, 'E', 0),
                (80, 'F', 1), (112, 'G', 2), (88, 'H', 0), (104, 'I', 0), (120, 'J', 1),
                (116, 'K', 0)
            ]

    rebalanced_right_heavy_right_child_right_heavy_node_list = ['C', 'A', 'G', 'B', 'F', 'I', 'J', 'D', 'E', 'H', 'K']
    
    right_heavy_right_child_left_heavy_bst = [
                (64, 'A', 4), (32, 'B', 1), (96, 'C', 3), (16, 'D', 0), (48, 'E', 0),
                (80, 'F', 2), (112, 'G', 1), (72, 'H', 0), (88, 'I', 1), (120, 'J', 0),
                (84, 'K', 0)
            ]

    rebalanced_right_heavy_right_child_left_heavy_node_list = ['F', 'A', 'C', 'B' ,'H', 'I', 'G', 'D', 'E', 'K', 'J']

    left_heavy_left_child_left_heavy_bst = [
                (64, 'A', 4), (32, 'B', 3), (96, 'C', 1), (16, 'D', 2), (48, 'E', 1),
                (80, 'F', 0), (112, 'G', 0), (8, 'H', 0), (24, 'I', 1), (56, 'J', 0),
                (20, 'K', 0)
            ]
    rebalanced_left_heavy_left_child_left_heavy_node_list = ['B', 'D', 'A', 'H', 'I', 'E', 'C', 'K', 'J', 'F', !!'G']

    left_heavy_left_child_right_heavy_bst = [
                (64, 'A', 4), (32, 'B', 3), (96, 'C', 1), (16, 'D', 1), (48, 'E', 2),
                (80, 'F', 0), (112, 'G', 0), (8, 'H', 0), (40, 'I', 0), (56, 'J', 1),
                (52, 'K', 0)
            ]

    rebalanced_left_heavy_left_child_right_heavy_node_list = ['E', 'B', 'A', 'D', 'I', 'J', 'C', 'H', 'K', 'F', 'G']

    def build_unbalanced_tree(self, bst, node_list):
        for node in node_list:
            new_node = Node(node[0], node[1])
            new_node.height = node[2]
            if bst.root == None:
                bst.root = new_node
            else:
                current_node = bst.root
                while current_node:
                    if new_node.key <= current_node.key:
                        if current_node.left_child == None:
                            new_node.parent = current_node
                            current_node.left_child = new_node
                            break
                        else:
                            current_node = current_node.left_child
                    else:
                        if current_node.right_child == None:
                            new_node.parent = current_node
                            current_node.right_child = new_node
                            break
                        else:
                            current_node = current_node.right_child
        return bst
    
    @pytest.mark.parametrize('parent_node, parent_height, left_node, left_node_height, right_node, right_node_height',
                        [
                            (Node(50, 'A'), 6, Node(25, 'B'), 5, Node(75, 'C'), 5),
                            (Node(50, 'A'), 6, Node(25, 'B'), 3, Node(75, 'C'), 5),
                            (Node(50, 'A'), 6, Node(25, 'B'), 5, Node(75, 'C'), 3),
                            (Node(50, 'A'), 6, None, None, Node(75, 'C'), 5),
                            (Node(50, 'A'), 6, Node(25, 'B'), 5, None, None)
                        ])
    def test_update_height(self, parent_node, parent_height, left_node, left_node_height, right_node, right_node_height):
        bst = BST()
        if left_node:
            left_node.height = left_node_height
        if right_node:
            right_node.height = right_node_height
        
        parent_node.left_child = left_node
        parent_node.right_child = right_node

        bst.root = parent_node

        bst.update_height(bst.root)

        assert bst.root.height == parent_height


    

    @pytest.mark.parametrize('parent_node, parent_bf, left_node, left_node_height, right_node, right_node_height',
                        [
                            (Node(50, 'A'), 0, Node(25, 'B'), 5, Node(75, 'C'), 5),
                            (Node(50, 'A'), 2, Node(25, 'B'), 3, Node(75, 'C'), 5),
                            (Node(50, 'A'), 2, Node(25, 'B'), 5, Node(75, 'C'), 3),
                            (Node(50, 'A'), 6, None, None, Node(75, 'C'), 5),
                            (Node(50, 'A'), 6, Node(25, 'B'), 5, None, None)
                        ])
    def test_update_balance_factor(self, parent_node, parent_bf, left_node, left_node_height, right_node, right_node_height):
        bst = BST()
        if left_node:
            left_node.height = left_node_height
        if right_node:
            right_node.height = right_node_height
        
        parent_node.left_child = left_node
        parent_node.right_child = right_node

        bst.root = parent_node

        assert bst.get_balance_factor(bst.root) == parent_bf

        
    def populate_bst(self, bst, node_list):
        print(node_list)
        for node in node_list:
            #print(f'adding: {node[1]}')
            bst.put(node[0], node[1])
        bst.breadth_first_traversal()
    
    @pytest.mark.parametrize('node_list, rebalanced_node_list',
                        [
                            (right_heavy_right_child_right_heavy_bst, rebalanced_right_heavy_right_child_right_heavy_node_list),
                            (right_heavy_right_child_left_heavy_bst, rebalanced_right_heavy_right_child_left_heavy_node_list),
                            (left_heavy_left_child_left_heavy_bst, rebalanced_left_heavy_left_child_left_heavy_node_list),
                            (left_heavy_left_child_right_heavy_bst, rebalanced_left_heavy_left_child_right_heavy_node_list)
                        ])
    def test_rebalance(self, node_list, rebalanced_node_list):
        # All test trees are unbalacned about root.
        bst = BST()
        self.build_unbalanced_tree(bst, node_list)      
        #bst.breadth_first_traversal()  
        bst.rebalance(bst.root)
        #print(bst.breadth_first_traversal())
        #assert abs(bst.root.left_child.height - bst.root.right_child.height) <= 1
        assert bst.breadth_first_traversal() == rebalanced_node_list

    def test_left_rotation(self):
        # NOTE: SHOULD COME UP WITH TEST TO TEST NON ROOT UN BALANCE
        # All test trees are unbalanced about root
        bst = BST()
        self.build_unbalanced_tree(bst, self.right_heavy_right_child_right_heavy_bst)
        bst.left_rotation(bst.root)
        print(f'lc-height: {bst.root.left_child.height}, rc-height: {bst.root.right_child.height}')
        assert bst.root.left_child.height - bst.root.right_child.height == 0

    def test_right_rotation(self):
        # NOTE: SHOULD COME UP WITH TEST TO TEST NON ROOT UN BALANCE
        # All test trees are unbalanced about root
        bst = BST()
        self.build_unbalanced_tree(bst, self.left_heavy_left_child_left_heavy_bst)
        bst.right_rotation(bst.root)
        print(f'lc-height: {bst.root.left_child.height}, rc-height: {bst.root.right_child.height}')
        assert bst.root.left_child.height - bst.root.right_child.height == 0

    








