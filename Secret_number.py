import sys
input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())
    ans = []

    p = 10 

    for _ in range(1, 19):  
        d = p + 1           
        if d > n:
            break

        if n % d == 0:
            ans.append(n // d)

        p *= 10

    if not ans:
        print(0)
    else:
        ans.sort()
        print(len(ans))
        print(*ans)
