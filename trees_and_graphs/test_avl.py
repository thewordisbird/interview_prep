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
    assert n.height == 0




# Tests for BST Class
@pytest.fixture(scope='module')
def empty_bst():
    return BST()

@pytest.fixture(scope='module')
def rooted_bst():
    bst = BST()
    bst.put(6, 'A')
    return bst

def test_bst_construction():
    bst = BST()
    assert bst.root == None
    assert bst.size == 0

def test_check_balance_factor():
    pass

@pytest.mark.parametrize('new_node, parent, root_height', 
                            [
                                (Node(3, 'B'), 'A', 1),
                                (Node(9, 'C'), 'A', 1),
                                (Node(2, 'D'), 'B', 2),
                                (Node(4, 'E'), 'B', 2),
                                (Node(10, 'F'), 'C', 2)
                            ])
def test__put(rooted_bst, new_node, parent, root_height):
    print(rooted_bst.size)
    rooted_bst._put(new_node, rooted_bst.root)
    assert new_node.parent.value == parent
    assert rooted_bst.root.height == root_height

def test_put_root(empty_bst):
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
def test_put(empty_bst, key, value, size):
    empty_bst.put(key, value)
    assert empty_bst.size == size


