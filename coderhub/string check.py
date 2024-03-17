def stringCheck(value) :
    for i in range(len(value)) :
        if value[i]==value[i+1]:
            return True
        else :
            return False
print("Please enter list  = ")
value = input().split(',')
value=[element.strip() for element in value]

#h = int(input())
a = stringCheck(value)
print(a)