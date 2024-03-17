from typing import List
def get_duplicate_elements(arr: List[int]) -> List[int]:
    # write your code here ^_^
    dup=[]
    
    for i in range(len( arr)):
            if arr[i] in arr[i+1:] and arr[i] not in dup:
                 dup.append(arr[i])
    return dup 


print(get_duplicate_elements([2,3,2,3]))