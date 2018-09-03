list_name=[]
score_list=[]
dict={}
n=int(input())
for i in range(n):
    list_name.append(input())
    score_list.append(float(input()))
    dict[list_name[i]]=score_list[i]
print(dict)
score_list2=score_list
z=max(score_list2)
while max(score_list2)==z:
    score_list2.remove(max(score_list2))
y=(max(score_list2))

