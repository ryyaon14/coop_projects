'''from datetime import datetime , timedelta

def kSumSubset(dateString) :
    t=datetime.now()
    tyear= timedelta(days=4*365)
    t200=timedelta(days=200 * 365)
    d =dateString
    day= d[8:9]
    mounth = d[5:6]
    year = d[0:3]


    if t.day()<int(day):
        return 'false'
    elif t.year>=int(tyear):
        return 'false'
    elif t.year<=int(t200) :
        return 'false'
    else : 
        return ;'true'

print("please enter NUMBER = ")
#w= input()
h=(input()) 
a= kSumSubset( h)
print ( a )
'''

from datetime import datetime, timedelta

def kSumSubset(dateString):
    t = datetime.now()
    tyear = timedelta(days=4 * 365)
    t200 = timedelta(days=200 * 365)
    d = dateString
    day = d[8:10]
    month = d[5:7]
    year = d[0:4]

    if t.day < int(day):
        return 'false'
    elif t.year <= int(year) + tyear.days // 365:
        return 'false'
    elif t.year <= int(year) - t200.days // 365:
        return 'false'
    else:
        return 'true'

print("Please enter NUMBER = ")
#w = input()
h = input()
a = kSumSubset(h)
print(a)


