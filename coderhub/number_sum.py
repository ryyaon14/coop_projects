def number_sum(num):
    t =0
    for i in num:
        t+=int(i)
        return t
    
a=int(input('enter number = ' ))   
b= number_sum(a)
print ( b)

