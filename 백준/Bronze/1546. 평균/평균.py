n=int(input())
score_list=list(map(int, input().split()))
max_score=max(score_list)

new_list=[]
for a in score_list :
    new_list.append(a/max_score * 100)
result=sum(new_list)/n 

print(result)