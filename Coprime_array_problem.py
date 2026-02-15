import math
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    found = -1
    for x in range(2, 60): 
        ok = False
        for v in a:
            if math.gcd(v, x) == 1:
                ok = True
                break
        if ok:
            found = x
            break

    print(found)
