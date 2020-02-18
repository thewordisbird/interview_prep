def nocross(a,b):
    dp = []
    for i in range(len(a)):
    
        if i == 0:
            connection = nearest_connection(a[i], b)
        else:
            connection = nearest_connection(a[i], b, dp[-1])

        if connection != None:
            dp.append(connection)

    return len(dp)

def nearest_connection(a, arr_b, greater_than=-1):
    for i in range(greater_than + 1, len(arr_b)):
        if abs(a - arr_b[i]) <= 4:
            return i
    return None


if __name__ == "__main__":
    a = [1, 2, 3, 4, 6, 5]
    b = [2, 5, 4, 3, 6, 1]

    print(nocross(a,b))