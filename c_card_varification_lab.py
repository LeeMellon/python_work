"""Instructions

1. Slice off the last digit.  That is the **check digit**.
2. Reverse the digits.
3. Double every other element in the reversed list.
4. Subtract nine from numbers over nine.
5. Sum all values.
6. Take the second digit of that sum.
7. If that matches the check digit, the whole card number is valid.
"""

master_s = '4  5  5  6  7  3  7  5  8  6  8  9  9  8  5  5' #raw data CC number
master_l = []                                               #makes list type of master_s
check_val = []                                              #the validation check digit
rev = []                                                    #master_l reversed
last = []                                                   #every other num doubled
nums = []                                                   #digits less 9
def funk_1():
    master_l = master_s.split()                             #splits master string into list
    check_val = master_l[-1]                                #takes out the reference digit
    for i in master_l:
        rev.append(int(i))                                  #casts str of nums as ints
        rev.reverse()                                       #reverses list order
    for i in rev[1::2]:                                     #iterates through every other digit
        x = i*2                                             #multiplies every other digit by 2
        last.append(x)                                      #appends to list last
    for i in last:
        if i > 9:                                           #iterates through last, looking for nums >9
            y = i-9
            nums.append(y)                                  #subtracts 9 and appends to list nums
    a = str(sum(nums))                                      #sums list nums and recasts to str
    b = a[1]                                                #takes out the second digit from nnums for validation check
    if b == check_val:                                      #chacks validation
        print("Valid Card")
    elif b != check_val:
        print("Not Valid")


funk_1()
