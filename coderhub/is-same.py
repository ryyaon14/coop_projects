def is_same(name1, name2):
    if (name1==name2) :
        return "they are the same"
    else :
        return "they are not the same" 

print("please enter the two names = ")
w= input()
h=input() 
a= is_same( w, h)
print ( a )