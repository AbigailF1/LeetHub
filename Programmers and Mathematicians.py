n = int(input())
for i in range(n):
    a, b = list(map(int, input().split()))
    print(min (a, b , (a+b)//4))
