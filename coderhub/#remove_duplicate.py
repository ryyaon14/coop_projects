#remove_duplicate
from typing import List
def remove_duplicate(arr: List[int]) -> List[int]:
    # write your code here ^_^
    RemDup=list(set(arr))
    newarr=sorted(RemDup)
    formatted_result = ''.join(str(num) for num in newarr)
    array=[]
    array =formatted_result
    return array

print(remove_duplicate( [7,8,9,7]))

