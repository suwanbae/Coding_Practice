a=input()
n=len(a)
t=True

for i in range (0,n,1):
    if a[i] != a[n-i-1]:
       t=False
       break

if t:
    print(1)
else:
    print(0)