t = int(input())
for _ in range(t):
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    L = a.index(1)
    R = n - 1 - a[::-1].index(1)
    if R - L + 1 <= x:
        print("YES")
    else:
        print("NO")
