

LL= [[]]
L = [[]]
Spells = []
nbSpells = []

def product(args, repeat=1):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
    pools = [list(pool) for pool in args] * repeat
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    return result

def check_liste(a):
    if a == None:
        print("Please put the correct values")
        return input()
    else:
        return a

def fraction_list(a):
    nb = 0
    for i in range(len(a)):
        if i == 0:
            LL[nb].append(a[i])
        elif a[i][0] == a[i-1][0]:
            LL[nb].append(a[i])
        else:
            nb +=1
            LL.append([])
            LL[nb].append(a[i])
    return LL


def check_Spells(c):
    if not Spells:
        Spells.append(c)
        nbSpells.append(1)
    else: 
        for i in range (len(Spells)):
            if Spells[i] == c:
                nbSpells[i] += 1
                return True
        Spells.append(c)
        nbSpells.append(1)
    return False

def check_nbSpells():
    for i in nbSpells:
        if i != 2 :
            return False
    return True

def check(a):
    for i in a:
        for j in i:
            for c in j:
                check_Spells(c)
        if check_nbSpells() :
            return i
        else:
            Spells.clear()
            nbSpells.clear()
    return []

l = []
while(True):
    a = input()
    if a == "stop":
        break
    liste = [item for item in a.split()]
    l.append(liste)

a = l

a = check_liste(a)

a = list(product(fraction_list(a), repeat=1))



a = check(a)


if not a:
    print("mo pas conner")
else:
    print(a)

            
