from collections import defaultdict
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    matrix = []
    for rows in range(n):
        row_x = [int(num) for num in input().split()]
        matrix.append(row_x)
    dir1 = defaultdict(int)
    dir2 = defaultdict(int)
    for row in range(n):
        for col in range(m):
            dir1[row - col] += matrix[row][col]
            dir2[row + col] += matrix[row][col]
    summ = 0
    for row in range(n):
        for col in range(m):
            summ = max(summ, dir1[row - col] +
                       dir2[row + col] - matrix[row][col])
    print(summ)
