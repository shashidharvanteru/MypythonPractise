n = int(input())
arr=list(map(int,input().split()))[:n]
z=max(arr)
while max(arr)==z:
    arr.remove(max(arr))
print(max(arr))


