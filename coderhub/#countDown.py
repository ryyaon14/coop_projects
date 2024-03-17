#countDown
from typing import List
def countDown(number: int) -> str:
    # write your code here ^_^
    i=0
    stack=[]
    while i<= number:
        stack.append(str(i))
        i+=1
    rev=stack[::-1]    
    return ' '.join(rev)

print(countDown(10))