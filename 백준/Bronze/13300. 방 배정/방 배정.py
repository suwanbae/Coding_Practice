n,k=map(int, input().split()) 
students=[] 
total_rooms=0  

for _ in range(2):
    students.append([0]*6) 
    
for _ in range(n):
    s,y= map(int, input().split())
    students[s][y-1]+=1
    
for i in range(2):
    for j in range(6):
        count=students[i][j] 
        if count != 0: 
            total_rooms+=(count+k-1)//k
        
print(total_rooms)