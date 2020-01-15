def min_steps(pts):
    step_count = 0
    # Don't need to evaluate final point.
    for i in range(len(pts) - 1):
        print(i)
        print(f'evaluating steps from {pts[i]} to {pts[i+1]}')
        step_count += steps(pts[i], pts[i+1])
        

    return step_count

def steps(start_point, end_point):
    x_dif = abs(start_point[0] - end_point[0])
    y_dif = abs(start_point[1] - end_point[1])
    diag_steps = min(x_dif, y_dif)
    straigt_steps = max(x_dif, y_dif) - diag_steps
    return diag_steps + straigt_steps

if __name__ == "__main__":
    # Test steps function
    #pt_1 = (0,0)
    #pt_2 = (0, 5)
    #print(steps(pt_1, pt_2))

    pts = [(0,0), (1,1), (-2,1), (-3,-2), (2,-1), (2,3)]
    #print(steps(pts[0], pts[1]))
    #print(steps(pts[1], pts[2]))
    print(min_steps(pts))