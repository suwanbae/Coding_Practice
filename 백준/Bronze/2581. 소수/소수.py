m=int(input())
n=int(input())
sosu=[]
for number in range (m, n+1):
    if number <2:
        continue

    for j in range (2,number,1):
        if number % j == 0:
            break

    else:  
        sosu.append(number)
    
if not sosu: 
    print(-1)

else:
    total=sum(sosu)
    min_sosu=min(sosu)
    print(total)
    print(min_sosu)