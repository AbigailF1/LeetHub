t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    check = True
    for i in range(n-1):
        if (arr[i + 1] - arr[i]) >= 2:
            check = False
    if check:
        print("YES")
    else:
        print("NO")
