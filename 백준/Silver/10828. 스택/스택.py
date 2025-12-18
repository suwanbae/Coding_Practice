import sys
N = int(input())
stack = []
for i in range(N):
    command = sys.stdin.readline().split()
    ctype = command[0]
    if ctype == "push":
        stack.append(command[1])
    elif ctype == "pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    elif ctype == "top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    elif ctype == "size":
        print(len(stack))
    elif ctype == "empty":
        if not stack:
            print(1)
        else:
            print(0)