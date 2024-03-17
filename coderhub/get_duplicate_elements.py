def get_duplicate_elements(arr) :
    seen = []
    duplicate =[]
    i=0
    while i <=(len(arr )-1):
        if arr[i] in seen: 
            i+=1
        else :
            seen[i]=arr[i]
            duplicate[i]=+1

        i+=1

        
    return the max duplicated[i] with its number in seen[i]
