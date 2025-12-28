n = int(input())
for i in range(n):
    a, b = map(str, input().split())
    new_a=sorted(a)
    new_b=sorted(b)

    if new_a == new_b:
        print("Possible")
    else:
        print("Impossible")