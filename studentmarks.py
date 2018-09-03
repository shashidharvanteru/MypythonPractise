student_dict={}
i=0
count=0
s=0
n=int(input())
for _ in range(n):
    name,*line=input().split()
    scores=list(map(float,line))
    student_dict[name]=scores
query_name=input()
l=list(student_dict.get(query_name))
s=float(sum(l))
s=s/len(l)
print("%.2f" %s)

