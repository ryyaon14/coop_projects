from typing import List
import math
def sum_even(arr: List[int]) -> int:
    # write your code here ^_^
    evenarr=[]
    for i in arr:
        if i%2==0:
            evenarr.append(i)

    s=sum(evenarr)
    return s

print(sum_even( [1,3,7]))
