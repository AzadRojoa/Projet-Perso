Equiper = []
Spells = []
nbSpells = []
L=[]

def test(Equiper, l):
    for i in Equiper:
        L.append(i)
        for j in l :
            L.append


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
b = input("Combien de node equiper? ")
for i in range(int(b)):
    a = input("Node equiper: ")
    liste = [item for item in a.split()]
    Equiper.append(liste)
while(True):
    a = input("Autre node: ")
    liste = [item for item in a.split()]
    l.append(liste)
    if a == "stop":
        break
print(Equiper)
#a = l



#a = list(product(fraction_list(a), repeat=1))
#print (a)



#a = check(a)


#if not a:
#    print("mo pas conner")
#else:
#    print(a)

            
