T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())

    apt = [[0] * n for _ in range(k + 1)]

    for j in range(n):
        apt[0][j] = j + 1

    for i in range(1, k + 1):
        for j in range(n):
            if j == 0:
                apt[i][j] = apt[i-1][j]
            else:
                apt[i][j] = apt[i-1][j] + apt[i][j-1]

    print(apt[k][n-1])