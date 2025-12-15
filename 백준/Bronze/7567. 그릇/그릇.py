t = input().strip()

total = 10
prev_char = t[0]

for i in range(1, len(t)):
    current_char = t[i]
    
    if current_char == prev_char:
        total += 5
    else:
        total += 10
        
    prev_char = current_char

print(total)