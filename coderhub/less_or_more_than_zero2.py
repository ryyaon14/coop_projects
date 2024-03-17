def less_or_more_than_zero(x:int):
    
    place: str
    if x==0:
        place = 'Equal to zero '
    elif x>=0 :
        place = 'Greater than Zero'
    else:
       place = 'Less than zero'
    return print(place)
less_or_more_than_zero(20)
    