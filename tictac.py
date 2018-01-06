def game():
    main = {'a': ['a'], 'b': ['b'], 'c': ['c'], 'd': ['d'], 'e': ['e'], 'f': ['f'], 'g': ['g'], 'h': ['h'], 'i': ['i'],
            'win': False, 'count': 0}

    def replay():
        replay = input("would you like to play again? (Y/N): ").capitalize()
        if replay == 'Y':
            game()
        elif replay == 'N':
            print("Good bye")

    def wincheck():
        if main['a'] == 'X' and main['b'] == 'X' and main['c'] == 'X':
            main['win'] = True
            bprint()
            replay()
        elif main['a'] == 'O' and main['b'] == 'O' and main['c'] == 'O':
            main['win'] = True
            bprint()
            replay()
        elif main['d'] == 'X' and main['e'] == 'X' and main['f'] == 'X':
            main['win'] = True
            bprint()
            replay()
        elif main['d'] == 'O' and main['e'] == 'O' and main['f'] == 'O':
            main['win'] = True
            bprint()
            replay()
        elif main['g'] == 'X' and main['h'] == 'X' and main['i'] == 'X':
            main['win'] = True
            bprint()
            replay()
        elif main['g'] == 'O' and main['h'] == 'O' and main['i'] == 'O':
            main['win'] = True
            bprint()
            replay()
        elif main['a'] == 'X' and main['d'] == 'X' and main['g'] == 'X':
            main['win'] = True
            bprint()
            replay()
        elif main['a'] == 'O' and main['d'] == 'O' and main['g'] == 'O':
            main['win'] = True
            bprint()
            replay()
        elif main['b'] == 'X' and main['e'] == 'X' and main['h'] == 'X':
            main['win'] = True
            bprint()
            replay()
        elif main['b'] == 'O' and main['e'] == 'O' and main['h'] == 'O':
            main['win'] = True
            bprint()
            replay()
        elif main['c'] == 'X' and main['f'] == 'X' and main['i'] == 'X':
            main['win'] = True
            bprint()
            replay()
        elif main['c'] == 'O' and main['f'] == 'O' and main['i'] == 'O':
            main['win'] = True
            bprint()
            replay()
        elif main['a'] == 'X' and main['e'] == 'X' and main['i'] == 'X':
            main['win'] = True
            bprint()
            replay()
        elif main['a'] == 'O' and main['e'] == 'O' and main['i'] == 'O':
            main['win'] = True
            bprint()
            replay()
        elif main['c'] == 'X' and main['e'] == 'X' and main['g'] == 'X':
            main['win'] = True
            bprint()
            replay()
        elif main['c'] == 'O' and main['e'] == 'O' and main['g'] == 'O':
            main['win'] = True
            bprint()
            replay()
        elif main['a'] == 'X' and main['c'] == 'X' and main['g'] == 'X' and main['i'] == 'X':
            main['win'] = True
            bprint()
            replay()
        elif main['a'] == 'O' and main['c'] == 'O' and main['g'] == 'O' and main['i'] == 'O':
            main['win'] = True
            bprint()
            replay()
        else:
            pass

    def cat():
        count = 0

        for v in main:
            if main[v] == 'X' or main[v] == 'O':
                count += 1
                # if main[v] == 'O':
                #     main['count'] += 1
        print(count)
        if count < 9:
            count = count * 0
            print(count)
        elif count == 9:
            print("Cat's Game! Start again")
            replay()

    def bprint():
        board = ("{}   ||   {}   ||   {}\n"
                 "------------------\n"
                 "{}   ||   {}   ||   {}\n"
                 "------------------\n"
                 "{}   ||   {}   ||   {}").format(main['a'], main['b'], main['c'], main['d'], main['e'], main['f'],
                                                  main['g'],
                                                  main['h'], main['i'])
        print(board)

    name1 = input('Who is playing X? ')
    name2 = input("Who is playing O? ")

    while main['win'] == False:
        bprint()
        point = input("{} where do you want to place your X?: ".format(name1))
        main[point] = 'X'
        wincheck()
        cat()
        bprint()
        point = input("{} where do you want to place your O?: ".format(name2))
        main[point] = 'O'
        wincheck()
        cat()
    else:
        replay()

game()
