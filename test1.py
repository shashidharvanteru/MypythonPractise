import numpy as np
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9],np.int32)
arr1=np.array([],np.int32)
np.copyto(arr,arr1,where=len(arr)!=0)
np.place(arr1,arr1%2==1,[-1])
print(arr1)
print(arr)

