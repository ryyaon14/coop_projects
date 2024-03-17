from typing import List
def calculate_sum(lst: List[int]) -> int:
    # write your code here ^_^
    s=0
    for i in lst:
        if int(i)==7:
            return s
        else : 
            s+=int(i)

    return s

print (calculate_sum([1,2,4,5,6,7]))


