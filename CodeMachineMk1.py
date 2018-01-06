# def clean_number():
#     num = input("what is the number you want to format?: ")
#     ara = num[0:3]
#     pre = num[3:6]
#     suf = num[6:10]
#     print("({})-{}-{}".format(ara, pre, suf))


class Code:
    def __init__(self):                     #Bring my creation to LIFE!!
        # self.name = name
        self.code_indx = {' ': 0}           #
        self.control = {' ': 0}
        self.code_strip = []
        self.clean_letters = []
        self.code_inv = {}
        self.message = []
        self.num = 0

    def __del__(self):
        "delete a thing"

    def code_console(self):
        while True:
            q = input( '(E)ncode, (D)ecode, or (Q)uit'  ).lower()
            if q == "e":
                self.num = int( input( "what ROT do you want ro encode with?  " ) )
                self.code_list( self.num )
                self.intake()
            elif q == 'd':
                self.de_code()
            elif q == 'q':
                break

    def invert_dict(self):
        val = []
        key = []
        for i in self.code_indx.values():
            key.append( i )
        for k in self.code_indx.keys():
            val.append( k )
        self.code_inv = dict( zip( key, val ) )
        # print(self.code_inv)

    def code_list(self, num):
        counter = 1
        letts = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in letts[num::]:
            self.code_indx[i] = counter
            counter += 1
            if counter >= 27:
                break
        # print(self.code_indx)
        self.invert_dict()

    def control_list(self):
        counter = 1
        letts = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for i in letts:
            control[i] = counter
            counter += 1
            if counter >= 27:
                break

    def intake(self):
        letters_list = []
        raw_data = input( 'input your message here: ' )
        for i in raw_data:
            letters_list.append( i )
        # print(letters_list)
        for letter in letters_list:
            self.code_strip.append( self.code_indx[letter] )
            # break
        # print(self.code_strip)
        # print(self.code_inv)

    def de_code(self):
        # print(self.code_inv)
        for num in self.code_strip:
            self.clean_letters.append( self.code_inv[num] )
        # print(self.clean_letters)
        self.message =''.join( self.clean_letters )
        print(self.message)
        # for lett in self.clean_letters:
        #     self.message.append(lett)
        #     print(self.message)


Ian = Code()
Ian.code_console()
