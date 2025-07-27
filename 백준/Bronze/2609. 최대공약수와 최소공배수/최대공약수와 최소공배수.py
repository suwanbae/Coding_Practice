a,b = map(int,input().split())
def gys(a,b):
    if (a<b):
        a,b = b,a 
    while(b!=0):
        a,b = b,a%b
    return a
result = gys(a,b)
print(result, a*b//result, sep='\n')