def Decimal_places(num):
    nums=str(num) 
    for i in range(len(nums)):
        if nums[i]=='.':
            return (len(nums)-1-i)
        
       
    return '0'
        
print("Please enter NUMBER = ")
#w = input()
h = float(input())
a = Decimal_places(h)
print(a)
