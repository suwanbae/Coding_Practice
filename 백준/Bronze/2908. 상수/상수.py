a, b = input().split()
reversea = int(a[::-1])
reverseb = int(b[::-1])

print(max(reversea, reverseb))