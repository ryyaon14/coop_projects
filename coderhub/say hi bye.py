def say_hi_bye(name, num) :
    if num == 0:
        print('bye '+ name)
    else :
        print ('hi '+name )

print("Please enter Name then number 0 or 1 = ")
w = input()
h = int(input())
a = say_hi_bye(w,h)
print(a)