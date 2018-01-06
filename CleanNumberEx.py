"""takes raw data input and returns formatted phone number"""
def clean_number():
    num = input("what is the number you want to format?: ")
    ara = num[0:3]
    pre = num[3:6]
    suf = num[6:10]
    print("({})-{}-{}".format(ara, pre, suf))
