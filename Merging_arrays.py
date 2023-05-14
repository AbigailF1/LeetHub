n, m = map(int, input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr = []
l1, l2 = 0, 0
while l1 < n and l2 < m:
    if arr1[l1] >= arr2[l2]:
        arr.append(arr2[l2])
        l2 += 1
    else:
        arr.append(arr1[l1])
        l1 += 1
while l1 < n:
    arr.append(arr1[l1])
    l1 += 1
while l2 < m:
    arr.append(arr2[l2])
    l2 += 1

print(*arr)
