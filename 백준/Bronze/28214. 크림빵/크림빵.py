n, k, p = map(int, input().split())

breads = list(map(int, input().split()))

sell=0

for i in range (n):
    start=i*k
    end=start+k 
    current=breads[start:end]
    no_cream=current.count(0)
    
    if no_cream < p :
        sell += 1 
        
print(sell)