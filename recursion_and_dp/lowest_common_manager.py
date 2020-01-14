
def build_tree(top_manager, report_one, report_two):
    manager_tree = {}
    start = ord(top_manager)
    end = max(ord(report_one), ord(report_two)) - start

    i = 0
    while i <= end:
        manager_tree[i] = chr(i + start)
        i += 1

    return manager_tree

def lowest_common_manger(top_manager, report_one, report_two):
    manager_tree = build_tree(top_manager, report_one, report_two)
    node_index = ord(report_one) - ord(top_manager)
    target_index = ord(report_two) - ord(top_manager)
    parent_index = get_parent_index(node_index)

    while parent_index >= 0:
        print(f'parent: {parent_index}')
        if get_left_child_index(parent_index) == node_index:
            # Explore right branch
            print('exploring right branch')
            common_node = _explore_branch(manager_tree, get_right_child_index(parent_index), target_index)
        else:
            print('exploring left branch')
            common_node = _explore_branch(manager_tree, get_left_child_index(parent_index), target_index)
            print(common_node)
        print(common_node)
        
        if common_node:
            print(f'returning {manager_tree[parent_index]}')
            return manager_tree[parent_index]
        
        node_index = parent_index
        parent_index = get_parent_index(parent_index)


deactivate



if __name__ == "__main__":
    # Test build tree
    top_manager = "A"
    report_one = "P"
    report_two = "W"

    # Test for build_tree()
    #print(build_tree(top_manager, report_one, report_two))

    print(lowest_common_manger(top_manager, report_one, report_two))
