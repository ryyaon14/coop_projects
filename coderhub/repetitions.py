def repetitions(s):
    i=0
    rep=1
    rept=[]
    while i <len(s)-1 :
        if s[i]==s[i+1] :
            i+=1
            rep+=1
          
        else : 
            rept.append(rep)
            rep=1
            i+=1
    rept.append(rep)
    
    return max(rept)

print("please enter word = ")
w= input()
# h=input() 
a= repetitions( w)
print ( a )

