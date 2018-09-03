x=int(input())
y=int(input())
z=int(input())
n=int(input())
clist=[]
i=0
j=0
k=0
for i in range(x+1):
    for j in range(y+1):
        for k in range(z+1):
            if i+j+k!=n:
                mlist=[i,j,k]
                clist.append(mlist)
print(clist)