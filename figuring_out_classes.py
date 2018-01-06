"""solving class inhertance questions I've had. Practicing via 
RPG character sheet model of Classes"""
import random


class CharacterSheet:
    def __init__(self, name):
        self.name = name
        self.cha = 0
        self.intl = 0
        self.strg = 0
        self.make_me = self.creat_char( name )
        self.send = self.send()

    def __repr__(self):
        return ( "{} has been created, with {} Charisma, {} Intelligence, {} Strength, and {} HP".format( self.name,
                                                                                                     self.cha,
                                                                                                 self.intl,
                                                                                                 self.strg, self.hp ) )

    # def __repr__(self):
    #     return poop

    def creat_char(self, name):
        self.name = name
        self.cha = random.randrange( 1, 20 )
        self.intl = random.randrange( 1, 20 )
        self.strg = random.randrange( 1, 20 )
        self.hp = random.randrange( 1,30)
    def send(self):
        gameMaster.char_box.append( self )
        print( gameMaster.char_box )
        return gameMaster.char_box

class Table:
    def __init__(self):
        self.char_box = []
        self.char_folder = {}
    #
    # def __repr__(self):
    #     return ( [].format(gameMaster.char_box) )


gameMaster = Table()
Dingo = CharacterSheet( "Dingo" )
Spanker = CharacterSheet("Spanker")
Spanker.intl=29
print(Spanker)
print(gameMaster.char_box)