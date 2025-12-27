N = int(input())
result = []
while N > 0:
    result.append(N%2)
    N=N//2
result.reverse()
print("".join(map(str,result)))