'''
import datetime
def findAge(birthday):
    years= datetime.datetime.year() - birthday.datetime.year()
    
    month= datetime.datetime.month() - birthday.datetime.month()
    day=datetime.datetime.today() - birthday.datetime.day()
    
    age = (year*365)+(mounth*30)
    return age


x = findeAge('1999-2-16')
print (x)




'''

import datetime
#birthdays: {'name' : 'Rayan', 'birthdayy':'1999-02-16'}
entries = []
agess = []

def takeages():
    #print('how many people you have ? ')
    #x = int(input())
    
    #for s in range(x):
    s=1
    global count
    count=0
    while s!=0:
        count+=1
        print('please Enter name and bithday')
        

        birthdays={'name': input('Enter name : '), 'birthdayy':input('Enter birthday (YYYY-MMM-DD): ')}
        birthday= birthdays['birthdayy']
        entries.append(birthdays)
        
        print('Do you have entries ? ', '\n 1:yes        0 :No')
        s=int(input())
    print ('the numbers of entries is : ' , count )
    print("\n and the enrties is : ")
    return ( entries )

def findAge(entries):
    for s in entries:
        today = datetime.datetime.today()
        #birthday = datetime.datetime.strptime(entries, '%Y-%m-%d')
        
        name = s['name']
        date=datetime.datetime.strptime(s['birthdayy'], '%Y-%m-%d')
        
        age = today.year - date.year
        age_dic={'name': name, "age": age}
        agess.append(age_dic)
    # if today.month < birthday.month or (today.month == birthday.month and today.day < birthday.day):
      #  age -= 1
    
    return agess 
    

def findminmax(agess):
     
    if count ==1:
        print( "There is no oldest or youngest person" )
    else:
            
            age=[]
            for s in agess:
             age.append(s['age']) 

            maxx=max(age)
            minn=min(age)
            print(f"The oldest one is {maxx} years old and The youngest person here has  {minn} years old")





x = takeages()

print(x)
y = findAge(x)
print(y)
z = findminmax(y)
print(z)



'''

def findDay(birthday):
    birthday= datetime.datetime.strptime(birthday, '%Y-%m-%d')
    dayname= birthday.strftime('%Y-%b-%A')
    return dayname



def findmax(ages):
    
    return print ('The oldest one is ', ages.max(), ' old' )

def findmin(ages):
    return  print('The youngest person here has  ', ages.min(), ' old')

#x = findAge('1999-02-16')
#y = findDay('1999-02-16')
#print ('The Age is :  ',  x, "\nAnd the date is",  y ) 
x = takeages()

print(x)
y = findAge()
print(y)


'''
