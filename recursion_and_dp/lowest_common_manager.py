
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


def lowest_common_manager(top_manager, report_one, report_two):
    path_to_one = get_path(top_manager, report_one)
    path_to_two - get_path(top_manager, report_two)

    pointer = 0

    while pointer < len(path_to_one) and pointer < len(path_to_two):
        if path_to_one[pointer] == path_to_two[pointer]:
            pointer += 1
        
        elif pointer > 0:
            return path_to_one[pointer - 1]
        
        else:
            return None

def path_to_pointer(employee, target_report, path=[]):
    if employee == None:
        return False
    if employee == target_report:
        return True
    
    if employee:
        for report in employee.direct_reports:
            if path_to_pointer(report, target_report, path):
                path.append(report)

class Employee:
    def __init__(self, name, direct_reports):
        self.name == name
        self.direct_reports = []

    def add_direct_report(self, employee):
        self.direct_reports.append(employee)

class OrgChart:
    def __init__(self, top_manager):
        self.top_manager = None

    def build_org_chart(self, employees):
        for employee in employees:
            tmp_employee = Employee(employee)
            if self.top_manager == None:
                self.top_manager = employee
            for direct_report in employee:
                tmp_employee.add_direct_report(Employee(direct_report))



if __name__ == "__main__":
    # Test build tree
    top_manager = "A"
    report_one = "P"
    report_two = "W"

    # Test for build_tree()
    #print(build_tree(top_manager, report_one, report_two))

    print(lowest_common_manger(top_manager, report_one, report_two))

    # +++++ GENERAL SOLUTION - BY PATH COMPARISON +++++
    org_chart = {
                    'A': ['B', 'C', 'D'], 'B': ['E', 'F'], 'C': [], 'D': ['L', 'M', 'N'],
                    'E': [], 'F': ['G', 'H', 'I', 'J'], 'G': [], 'H': ['K'], 'I': [], 'J': [],
                    'K': [], 'L': [], 'M': ['O', 'P'], 'N': ['T', 'U'], 'O': [], 'P': ['Q', 'R', 'S'],
                    'Q': [], 'R': [], 'S': [], 'T':[], 'U': []

                    ]
                }

    # Remove classes and just use above dictionary as data structure. Search though it to find path