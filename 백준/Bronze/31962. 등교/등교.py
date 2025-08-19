n, x = map(int, input().split())

max_s = -1

for _ in range (n):
    s, t = map(int, input().split())
    
    if s + t <= x:
        max_s= max(max_s, s)
        
print(max_s)