t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    
    result = ""
    for a in s:
        result += a * r
    
    print(result)