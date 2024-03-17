from typing import List
def word_repeat(word: str, n: int) -> str:
    # write your code here ^_^
    i = 0
    stack=[]
    while i!=n:
        stack.append(word)
        i+=1
   
    return ' '.join(stack)
print(word_repeat('rayan', 3))