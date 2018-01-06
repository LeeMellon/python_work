names = ['Kieran', 'Suki', 'Alex', 'Serada', 'Jeff', 'Fin', 'Alfonzo']
people = [('Kieran', 'Prasch', 'Instructor'), ('Alfonzo', 'Ward', 'Student'), ('Fin', 'Balnik', 'Student')]

def n_length(x):
    l = []
    for i in names:
        if len(i) >= x:
            l.append(i)
    print(l)
n_length(7)

def s_start (n):
    l1 = []
    begin = [ l1.append(i) for i in names if i[0] == n.upper()]
    print(l1)

s_start("a")

def last_name():
    l2 = []
    poop = [l2.append(i[1])for i in people]


    print(l2)

last_name()

def string_list():
    l3 = []
    for i in people:
        for x in i:
            l3.append(x)
    print(l3)

string_list()