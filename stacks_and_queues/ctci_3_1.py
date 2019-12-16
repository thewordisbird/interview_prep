# Three In One: Describe how you could use a single array to implement 3 stacks.

# Discussion considerations & questions:
#   Do we know the max size required for each stack, or the total size allowed for the array?
#       If we do we could use a fixed size implementation where we split the array in 3 and use pointers to maintain our 3 stacks
#       If we don't and we need flexibility we can add a resize method that will shift the stacks when neeed. 
#       IDK IF THIS WORKS... Circular array. Figure out upon implementation

# Fixed Size Implementation:

# This implementation works. It's a little strange as all the callse are made throuhg the StackFixed object.
# Should probably re-structure to have calls made as a method of the substack.

class SubStackFixed:
    def __init__(self, start):
        self.start = start
        self.size = 0

class StackFixed:
    def __init__(self, stack_size):
        self.stack_list = [None for _ in range(stack_size * 3)]
        self.stack_size = stack_size

    def build_stacks(self):
        size = self.stack_size
        return SubStackFixed(0), SubStackFixed(size), SubStackFixed(size * 2)

    def add(self, stack, item):
        # Check for room in the stack:
        if stack.size == self.stack_size:
            print("Stack Full")
            return
        
        self.stack_list.insert(stack.size, item)
        stack.size += 1

    def pop(self, stack):
        item = self.stack_list[stack.size - 1]
        self.stack_list[stack.size - 1] = None
        stack.size -= 1
        return item

    def peek(self, stack):
        return self.stack_list[stack.size - 1]

    def is_empty(self, stack):
        return stack.size == 0


if __name__ == "__main__":
    stacks = StackFixed(30)
    stacks(stack_1).add('justin')
    print(stacks.stack_list)

