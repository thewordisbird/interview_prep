# Tower of Hanoi. 

def hanoi(disks, start, finish, aux,):
    if disks == 1:
        # Move disk to desired position
        print(f'Move disk from {start} to {finish}')
    
    else:

        # Simplify the problem by solving for disks - 1 to the desired
        # pole to free up the base
        hanoi(disks - 1, start, aux, finish)

        # Move the freed disk to the final position
        print(f'Move disk from {start} to {finish}')

        # Move the stack you moved to originally free up the bottom disk
        # ontop of the desired disk
        hanoi(disks-1, aux, finish, start)

    
if __name__ == "__main__":
    hanoi(3, 'A', 'B', 'C')