''' def logical_and(a, b):
    Logand= a and b
    return Logand

print("please enter  = ")
h= input()
x=bool(h)
z=input()
y=bool(z)
# h=input() 
a= logical_and(x,y)
print ( a )

print('please enter the name')
x=input().lower()
print(x)
'''
def logical_and(a, b):
    log_and = a and b
    return log_and

print("Please enter the first value:")
x = input().lower()  # Accept the input and convert it to lowercase

print("Please enter the second value:")
y = input().lower()  # Accept the input and convert it to lowercase

a = logical_and(x == "true", y == "true")  # Compare the input with "true" in a case-insensitive manner
print(a)