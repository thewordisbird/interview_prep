import pytest
# pytest --cov-report term-missing --cov=avl
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

@pytest.fixture(scope='function')
def populated_bst():
    bst = BST()
    nodes = [
                (70, 'A'), (31, 'B'), (93, 'C'), (14, 'D'), (73, 'E'), 
                (94, 'F'), (23, 'G'), (71, 'H'), (80, 'I'), (96, 'J'),
                (75, 'K'), (85, 'L'), (95, 'M'), (74, 'N'), (76, 'O'),
                (20, 'P'), (19, 'Q'), (35, 'R'), (81, 'S')
            ]
    populate_bst(bst, nodes)
    return bst

def populate_bst(bst, node_list):
        print(node_list)
        for node in node_list:            
            bst.put(node[0], node[1])    
        bst.breadth_first_traversal()

def test_bst_construction():
    bst = BST()
    assert bst.root == None
    assert bst.size == 0

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
rebalanced_left_heavy_left_child_left_heavy_node_list = ['B', 'D', 'A', 'H', 'I', 'E', 'C', 'K', 'J', 'F', 'G']

left_heavy_left_child_right_heavy_bst = [
            (64, 'A', 4), (32, 'B', 3), (96, 'C', 1), (16, 'D', 1), (48, 'E', 2),
            (80, 'F', 0), (112, 'G', 0), (8, 'H', 0), (40, 'I', 0), (56, 'J', 1),
            (52, 'K', 0)
        ]

rebalanced_left_heavy_left_child_right_heavy_node_list = ['E', 'B', 'A', 'D', 'I', 'J', 'C', 'H', 'K', 'F', 'G']


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

    @pytest.mark.parametrize('node_list, rebalanced_node_list',
                        [
                            (right_heavy_right_child_right_heavy_bst, rebalanced_right_heavy_right_child_right_heavy_node_list),
                            (right_heavy_right_child_left_heavy_bst, rebalanced_right_heavy_right_child_left_heavy_node_list),
                            (left_heavy_left_child_left_heavy_bst, rebalanced_left_heavy_left_child_left_heavy_node_list),
                            (left_heavy_left_child_right_heavy_bst, rebalanced_left_heavy_left_child_right_heavy_node_list)
                        ])
    def test_put(self, node_list, rebalanced_node_list):
        bst = BST()
        for node in node_list:
            bst.put(node[0], node[1])
        assert bst.breadth_first_traversal() == rebalanced_node_list


class TestBalance:
    
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
    def test_update_node_height(self, parent_node, parent_height, left_node, left_node_height, right_node, right_node_height):
        bst = BST()
        if left_node:
            left_node.height = left_node_height
        if right_node:
            right_node.height = right_node_height
        
        parent_node.left_child = left_node
        parent_node.right_child = right_node

        bst.root = parent_node

        bst.update_node_height(bst.root)

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
        bst.rebalance(bst.root)
        assert bst.breadth_first_traversal() == rebalanced_node_list

    def test_left_rotation(self):
        # NOTE: SHOULD COME UP WITH TEST TO TEST NON ROOT UN BALANCE
        # All test trees are unbalanced about root
        bst = BST()
        self.build_unbalanced_tree(bst, right_heavy_right_child_right_heavy_bst)
        bst.left_rotation(bst.root)
        print(f'lc-height: {bst.root.left_child.height}, rc-height: {bst.root.right_child.height}')
        assert bst.root.left_child.height - bst.root.right_child.height == 0

    def test_right_rotation(self):
        # NOTE: SHOULD COME UP WITH TEST TO TEST NON ROOT UN BALANCE
        # All test trees are unbalanced about root
        bst = BST()
        self.build_unbalanced_tree(bst, left_heavy_left_child_left_heavy_bst)
        bst.right_rotation(bst.root)
        print(f'lc-height: {bst.root.left_child.height}, rc-height: {bst.root.right_child.height}')
        assert bst.root.left_child.height - bst.root.right_child.height == 0

    
class TestDelete:
    @pytest.mark.parametrize('sub_root_key, min_node_key',
                            [
                                (70, 31),
                                (73, 14),
                                (93, 74)
                            ])
    def test_find_min(self, populated_bst, sub_root_key, min_node_key):
        bst = populated_bst
        sub_root_node = bst.get(sub_root_key)
        assert bst.find_min(sub_root_node).key == min_node_key

    @pytest.mark.parametrize('deleted_node, successor_node',
                            [
                                (14, None),
                                (76, None),
                                (23, 31),
                                (93, 94),
                                (73, 74),
                                (31, 35),
                                (85, 81)
                            ])
    def test_find_successor(self, populated_bst, deleted_node, successor_node):
        # Single Item Tree
        # Leaf Node (right & left)
        # Node with both children
        # Node with single child (right & left)
        node = populated_bst.get(deleted_node)
        if successor_node == None:
            assert populated_bst.find_successor(node) == None
        else:
            assert populated_bst.find_successor(node).key == successor_node

    @pytest.mark.parametrize('splice_node, parent_left, parent_right',
                            {
                                (14, None, 20),
                                (81, None, None),
                                (31, 35, 71)
                            })
    def test_splice(self, populated_bst, splice_node, parent_left, parent_right):
        # Leaf Node
        # Single Child (right & left)
        node = populated_bst.get(splice_node)
        parent = node.parent
        populated_bst.splice(node)
        if parent_left and parent_right:
            assert parent.left_child.key == parent_left
            assert parent.right_child.key == parent_right
        elif parent_left:
            assert parent.left_child.key == parent_left
            assert parent.right_child == parent_right
        elif parent_right:
            assert parent.left_child == parent_left
            assert parent.right_child.key == parent_right
        else:
            assert parent.left_child == parent_left
            assert parent.right_child == parent_right

    @pytest.mark.parametrize('deleted_node, left_child, right_child, successor_node',
                            [
                                (80, 75, 85, 81),
                            ])
    def test_insert_successor(self, populated_bst, deleted_node, left_child, right_child, successor_node):
        # Node has both children
        node = populated_bst.get(deleted_node)
        successor_node = populated_bst.get(successor_node)

        populated_bst.insert_successor(successor_node, node)
        assert successor_node.left_child.key == left_child
        assert successor_node.right_child.key == right_child

    @pytest.mark.parametrize('key',
                            [
                                (1), (100), (97)
                            ])
    def test_delete_key_not_found(self, populated_bst, key):
        with pytest.raises(KeyError):
            populated_bst.delete(key)
    
    @pytest.mark.parametrize('deleted_node',
                            [
                                (73), # Root node
                                (74), # Left leaf node
                                (35), # Right leaf node
                                (80), # Sub node with both children
                                (31), # Sub node with right child
                                (85), # Sub node with left child
                            ])
    def test_delete(self, populated_bst, deleted_node):
        pass


    def test_delete_key_error(self,populated_bst):
        
        with pytest.raises(KeyError):
            populated_bst.delete(69)

    def test_update_parent_height(self):
        pass

def display_post_order_traversal(bst):
    tree = bst.pre_order_traversal()
    for k, v in tree.items():
        if v['left'] and v['right']:
            print(f"Node: {k.key} | Left: {v['left'].key} | right {v['right'].key}")
        elif v['left']:
            print(f"Node: {k.key} | Left: {v['left'].key} | right None")
        elif v['right']:
            print(f"Node: {k.key} | Left: None | right {v['right'].key}")
        else:
            print(f"Node: {k.key} | Left: None | right None")







