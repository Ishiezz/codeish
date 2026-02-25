t = int(input())

for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    
    ones = sum(arr)
    
    min_lights = ones % 2
    max_lights = min(ones, 2*n - ones)
    
    print(min_lights, max_lights)
