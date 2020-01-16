
def build_tree_binary(top_manager, report_one, report_two):
    manager_tree = {}
    start = ord(top_manager)
    end = max(ord(report_one), ord(report_two)) - start

    i = 0
    while i <= end:
        manager_tree[i] = chr(i + start)
        i += 1

    return manager_tree

def lowest_common_manger_binary(top_manager, report_one, report_two):
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


def lowest_common_manager(org_chart, top_manager, report_one, report_two):
    print('finding path to one')
    path_to_one = get_path(org_chart, top_manager, report_one, [])
    print('finding path to two')
    path_to_two = get_path(org_chart, top_manager, report_two, [])

    print(path_to_one, path_to_two)

    lcm = None

    while len(path_to_one) > 0 and len(path_to_two) > 0:
        manager_one = path_to_one.pop()
        manager_two = path_to_two.pop()
        if manager_one == manager_two:
            lcm = manager_one
        
        else:
             break
    
    return lcm

def get_path(org_chart, employee, target_report, path=[]):
    print(path)
    if employee == target_report:
        return True
    if len(org_chart[employee]) == 0:
        return False

    for report in org_chart[employee]:
        if get_path(org_chart, report, target_report, path):
            path.append(employee)
            return path
    
    return path

if __name__ == "__main__":
    # Test build tree
    top_manager = "A"
    report_one = "P"
    report_two = "W"

    # Test for build_tree()
    #print(build_tree(top_manager, report_one, report_two))

    # +++++ GENERAL SOLUTION - BY PATH COMPARISON +++++
    org_chart = {
                    'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': [], 'D': ['L', 'M', 'N'],
                    'E': [], 'F': ['G', 'H', 'I', 'J'], 'G': [], 'H': ['K'], 'I': [], 'J': [],
                    'K': [], 'L': [], 'M': ['O', 'P'], 'N': ['T', 'U'], 'O': [], 'P': ['Q', 'R', 'S'],
                    'Q': [], 'R': [], 'S': [], 'T':[], 'U': []
                }

    #print(lowest_common_manager(org_chart, 'A', 'E', 'U'))

    # Test get_path
    print(get_path(org_chart, 'D', 'G'))

    print(lowest_common_manager(org_chart, 'A', 'P', 'S'))
    