def anagram():
    list1 = []
    list2 = []
    list3 = []  # had to make a list 3 because you can't change an object(like a list) that you're iterating through.
    word_1 = input( "Give me an word: " ).strip()
    word_2 = input( "Give me your proposed anagram: " ).strip()  # .strip() takes out extra spaces in the input
    ana_1 = word_1.replace( " ", "" ).lower()  # had to =ana_1 so that the work of replace would be saved
    ana_2 = word_2.replace( " ", "" ).lower()
    for let in ana_1:
        list1.append( let )
    for let in ana_2:
        list2.append( let )
    list3 = list1[::]
    # print(list1, list2)
    for i in list1:
        if i in list1 and i in list2:
            list3.remove( i )
            list2.remove( i )
    if len( list2 + list3 ) == 0:  # used len because None doesn't work
        print( "you've got a legit anagram!" )
    elif len( list2 + list3 ) != 0:  # None doesn't work because an empty list is still an object
        print( "Nope! You still have {} left".format( list3 + list2 ) )

        # print(list3, list2)


anagram()
