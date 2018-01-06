import random

shuffle = []
deck = []
players = []
inactive = []


class TestPlayer:
    def __init__(self, name, hand):
        self.name = name
        self.bank = 1000
        self.hand = hand
        self.bet = 0
        self.status = "active"

    def __repr__(self):
        return ('{} iS holding {}, with {} left and a bet of {}').format(self.name, self.hand, self.bank, self.bet)


class Player:
    def __init__(self, name):
        self.name = name
        self.bank = 1000
        self.hand = []
        self.bet = 0
        self.status = "active"

    def __repr__(self):
        return ('{} iS holding {}, with {} left, and a bet of {}').format(self.name, self.hand, self.bank, self.bet)


class SplitPlayer:
    def __init__(self, name, hand, bet):
        self.name = name
        self.bank = 0
        self.hand = hand
        self.bet = bet
        self.status = "split"

    def __repr__(self):
        return ('{} iS holding {}, with {} left and a bet of {}').format(self.name, self.hand, self.bank, self.bet)


class Dealer:
    def __init__(self, name):
        self.name = "Dealer"
        self.bank = 2000
        self.hand = []
        self.status = "Dealer"

    def __repr__(self):
        return ('The Dealer is showing {}').format(self.hand[0])


class Card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value

    def __repr__(self):
        return ('{}{}').format(self.face, self.suit)


def createDeck():
    suits = ['D', 'S', 'H', 'C']
    faceVal = [('A', 1), ('2', 2), ('3', 3), ('4', 4), ('5', 5), ('6', 6), ('7', 7), ('8', 8), ('9', 9), ('10', 10),
               ('J', 10), ('Q', 10), ('K', 10)]
    for suit in suits:
        for f, v in faceVal:
            shuffle.append(Card(suit, f, v))
    for card in shuffle:
        counter = len(shuffle)
        while counter > 0:
            x = random.randrange(counter)
            deck.append(shuffle[x])
            shuffle.pop(x)
            counter -= 1
    # print(deck, len(deck))
    return deck

def dealerShow():
    for player in players:
        if player.status != 'Dealer':
            pass
        elif player.status == 'Dealer':
            a = player.hand[0]
            # print('The Dealer is showing a {} of {}'.format(a.face, a.suit))
            return a


# def deal():
#     # print(top)
#     for player in players:
#         # top = len(deck)
#         while len(player.hand) < 2:
#             # x = random.randrange(top)
#             x = deck[0]
#             player.hand.append(x)
#             deck.remove(x)
#     # print(players, deck)
#     return players, deck


def deal(player):
        while len(player.hand) < 2:
            x = deck[0]
            player.hand.append(x)
            deck.remove(x)
        return player, deck


def firstRun():
    howmany = int(input('How many players are there?: '))
    for i in range(howmany):
        name = input('Player, what is your name? ')
        players.append(Player(name))
    # print(players)
    return players


def playerJoin():
    howmany = int(input('How many players are joining us?: '))
    for i in range(howmany):
        name = input('Player, what is your name? ')
        players.append(Player(name))
    # print(players)
    return players


def playerCrea():
    name = input('Player, what is your name? ')
    players.append(Player(name))


def dealerCrea():
    players.append(Dealer("Dealer"))
    return players


# def bet():
#     for player in players:
#         if player.status != "Dealer":
#             bid = int(input(('{} place your bet').format(player.name)))
#             player.bet = bid
#             player.bank -= bid
#     return players

def bet(player):
    if player.status != "Dealer" and player.status == 'active':
        bid = int(input(('{} place your bet').format(player.name)))
        player.bet = bid
        player.bank -= bid

    return player


def jackWin(player):
    player.status = 'jack'
    a = int(player.bet) * 2.5
    player.bank += a
    player.bet = 0
    print('{} has a BlackJack'.format(player.name))
    return player


# def jackCheck():
#     for player in players:
#         if player.name != 'Dealer':
#             a = player.hand[0]
#             b = player.hand[1]
#         if a.value == 10 and b.face == 'A':
#             jackWin(player)
#         elif a.face == 'A' and b.value == 10:
#             jackWin(player)
#         else:
#
#             pass

def jackCheck(player):
    if player.name != 'Dealer':
        a = player.hand[0]
        b = player.hand[1]
        if a.value == 10 and b.face == 'A':
            jackWin(player)
        elif a.face == 'A' and b.value == 10:
            jackWin(player)
        else:
            pass



def allHandSum():
    for player in players:
        x = 0
        run = range(x, len(player.hand))
        vals = []
        while x in run:
            card = player.hand[x]
            target = card.value
            vals.append(target)
            x += 1
        print(sum(vals))


def handSum(player):
    x = 0
    run = range(x, len(player.hand))
    vals = []
    while x in run:
        card = player.hand[x]
        target = card.value
        vals.append(target)
        x += 1
    amt = sum(vals)

    # print(amt)
    return (amt)

    # print("the len is", x)


def splitCheck(player):
    wages = player.bet
    card1 = player.hand[0]
    card2 = player.hand[1]
    target1 = card1.face
    target2 = card2.face
    if target1 == target2:
        q = input(("{} you have {}. Do you want to split? Y/N ").format(player.name, player.hand))
        if q == "y":
            name = player.name
            top = len(deck)
            x = random.randrange(top)
            splitCard = card2
            card3 = deck[x]
            deck.pop(x)
            card4 = deck[x]
            deck.pop(x)
            # player.status = "split"
            player.hand = [card1, card3]
            players.append(SplitPlayer(name, [splitCard, card4], wages))
            # print("split", players)
            return players, deck
        elif q == "n":
            pass


def testMonkey():
    c = Card('H', 'A', 1)
    d = Card('D', 'A', 1)
    players.append(TestPlayer("Monkey", (c, d)))

    # print(players)
    return players


def tree(player):
    show = dealerShow()
    if player.status == "active" or "split":
        name = player.name
        while handSum(player) <= 21:
            splitCheck(player)
            print("the dealer is showing", show)
            print('{} you have {}'.format(player.name, player.hand))
            q = input(("{} do you want to (H)it or (S)tand? ").lower().format(name))
            if q == 's':
                aceCheck(player)
                stand = handSum(player)
                print(("{} stands at {}").format(player.name, stand))
                return players
            elif q == 'h':
                top = len(deck)
                x = random.randrange(top)
                player.hand.append(deck[x])
                deck.pop(x)
        else:
            player.status = 'inactive'
            print("You're bust!")
            # players.remove(player)
            """doesn't work because iteration is by index
            If you remove a player it changes the index number
            of the next player
            Switched to status atribute"""
            # inactive.append(player)

            # print(player.status)
    elif player.status == 'jack':
        pass

    return player


def allTree():
    for player in players:
        if player.status != "Dealer":
            tree(player)


def dealCheck():
    for player in players:
        if player.status != 'Dealer':
            pass
        if player.status == 'Dealer':
            while handSum(player) <= 17:
                print('Dealer shows {}'.format(handSum(player)))
                top = len(deck)
                x = random.randrange(top)
                player.hand.append(deck[x])
                deck.pop(x)
            if handSum(player) > 21:
                print("dealer Busts with {} ".format(handSum(player)))
                player.status == "inactive"
            elif handSum(player) > 17 < 21:
                print('Dealer stands at', handSum(player))
    return player


def dealSum():
    for player in players:
        if player.name == 'Dealer':
            x = int(handSum(player))
            return x


def aceCheck(player):
    for card in player.hand:
        x = handSum(player)
        if x > 11:
            pass
        elif x <= 11 and card.face == "A":
            card.value = 11
    return player


def winner(player):
    player.bank += player.bet * 2
    print("{} you win! {}".format(player.name, player.bet * 2))


def loser(player):
    player.bank -= player.bet
    print(("{} you lose! You have {} left.").format(player.name, player.bank))


def pusher(player):
    player.bank += player.bet
    print(("Dealer pushes {}. You have {}").format(player.name, player.bank))


def splitCombo(player):
    if player.status != 'split':
        pass
    elif player.status == 'split':
        name = player.name
        bank = player.bank
        for player in players:
            if player.name == name and player.status != 'split':
                player.bank += bank
    return players


def splitKill(player):
    if player.status == 'split':
        players.remove(player)
    return players


def cleanUp():
    for player in players:
        splitCombo(player)
        splitKill(player)
    # print(players)
    return players


def winCheck():
    x = dealSum()
    for player in players:
        if player.name == 'Dealer':
            pass
        elif player.name != 'Dealer' and player.status == 'jacked':
            pass
        elif player.name != 'Dealer' and player.status == 'inactive':
            loser(player)
        elif player.name != 'Dealer' and player.status == 'active' or 'split':
            y = int(handSum(player))
            if y > 21:
                loser(player)
            elif x < 21 and x > y:
                loser(player)
            elif x > 21 or x < y:
                winner(player)
            elif x == y:
                pusher(player)
    # for player in players:
    #     splitCombo(player)
    # for player in players:
    #     splitKill(player)
    # print(players)
    return players

def statusUpdate(player):
    if player.status == 'Dealer':
        pass
    elif player.status != 'Dealer':
        q = input('{} you have {} in the bank. Do you want to continue? Y/N '.format(player.name, player.bank)).lower()
        if q == 'y':
            player.bet = 0
            player.status = 'active'
            player.hand = []
        elif q == 'n':
            players.remove(player)
            # player.bet = 0
            # player.status = 'inactive'
            # player.hand = []

# createDeck()
# dealerCrea()
# testMonkey()
# playerCrea()
# bet()
# deal()
# # splitCheck()
# jackCheck()
# # handSum()
# allTree()
# dealCheck()
# winCheck()
# cleanUp()


def gameTree():
    counter = 0
    while True:
        if counter == 0:
            firstRun()
            createDeck()
            dealerCrea()
            counter += 1
        elif counter > 0:
            createDeck()
            q = input('Is anyone joinig us? Y/N').lower()
            if q == 'y':
                playerJoin()
            elif q == 'n':
                pass
        for player in players:
            bet(player)
            deal(player)
            jackCheck(player)
        allTree()
        dealCheck()
        winCheck()
        cleanUp()
        for player in players:
            statusUpdate(player)



gameTree()