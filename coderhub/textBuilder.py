def textBuilder(expression:str) ->str:
    stack=[]
    for char in expression:
        if char !=']':
            stack.append(char)
        else :
            current=''
            while stack[-1]!='[':
                current=stack.pop() +current

            stack.pop()
            count=''
            while stack and stack[-1].isdigit():
                count = stack.pop() + count
            stack.append(current*int(count))

    return ''.join(stack)


result = textBuilder('3[a]2[bc]')
print("Result:", result)