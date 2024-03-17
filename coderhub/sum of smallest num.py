def sum_two_smallest_nums(arr):
    s=sorted(arr)
    return int(s[0])+int(s[1])

print("Please enter list  = ")
value = input().split(',')
value=[element.strip() for element in value]

#h = int(input())
a = sum_two_smallest_nums(value)
print(a)


