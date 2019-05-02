def change_making(d,n):
    solution = [float('inf') for _ in range(n + 1)]
    solution[0] = 0
    for i in range(n + 1):
        for coin in d:
            if coin <= i:
                solution[i] = min(solution[i], solution[i - coin] + 1)
    return -1 if solution[n] == float('inf') else solution[n]


if __name__ == "__main__":
    d=[1,3,4,5,6]
    n=10
    print(change_making(d,n))
    
    d=[1,2,4,6,8,10,22,23]
    n=40
    print(change_making(d,n))

    d=[1,2,10,11,12,15,19,30]
    n=1900
    print(change_making(d,n))

