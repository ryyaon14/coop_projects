phone_numbers = [  {'name' : 'Amal '     , 'number' : '1111111111' },
    {'name' : 'Mohammed ' , 'number' : '2222222222' }, 
    {'name' : 'Khadijah ' , 'number' : '3333333333' }, 
    {'name' : 'Abdullah ' , 'number' : '4444444444' }, 
    {'name' : 'Rawan '    , 'number' : '5555555555' }, 
    {'name' : 'Faisal '   , 'number' : '6666666666' }, 
    {'name' : 'Layla '    , 'number' : '7777777777' } ] 



def search_phone(num):
    print('Enter phone number: ')
    
    if not num.isdigit() or len(num)!=10:
        print('\n  This is invalid number! ')

    else :
        found=False
        for entry in phone_numbers :
            if entry['number']==num:
                found=True
                return entry['name']
            
            
        if not found:
            print('Sorry, the number is not there ')


x='2222222222'
print(search_phone(x))


