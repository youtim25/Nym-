import random

def enleve_baton(nb):
    for k in range(nb):
        L.pop(-1)
        
def verif_coup(nb):
    nb=int(input("le nombre de baton : "))
    while nb not in [1,2,3] and len(L)>nb:
        print("le coup n'est pas compté recommencez .")
        nb=int(input("le nombre de baton : "))
    return nb
def verif_win(t):
    if L == [] and t == 'ia':
        return 'J'
    if L == [] and t == 'j':
        return 'IA'
    return False
def J():
    print(L)
    print('Combien voulez vous retiré de baton 1,2 ou 3 baton')
    nb=verif_coup(0)
    enleve_baton(nb)
    return nb
    
def Ia_alea():
    print(L)
    nb=random.choice([1,2,3])
    while len(L)<nb:
        nb=random.choice([1,2,3])
    print(f"L'IA a retiré {nb} piéce")
    enleve_baton(nb)

def att(Jnb , Inb):
    if len(choix[Jnb-Inb-2]) >1:
        return random.choice(choix[len(L)-1])
    if choix[Jnb-Inb-2]== []:
        return random.choice([1,2,3])
def apprentissage(Jnb , Inb):
    print(Jnb , Inb)
    print(choix[Jnb-Inb-2])
    choix[Jnb+Inb-2].remove(Inb)
    
    
        

def Ia_intelligente(Jnb , Inb):
    print(L)
    nb=att()
    while len(L)<nb:
        nb=random.choice([1,2,3])
    print(f"L'IA a retiré {nb} piéce")
    enleve_baton(nb)
    return nb


choix = [[1,2,3],
         [1,2,3],
         [1,2,3],
         [1,2,3],
         [1,2,3],
         [1,2,3],
         [1,2,3],
         [1,2,3]]

while True:
    #t=random.choice(['ia','j'])
    t='j'
    L=['|','|','|','|','|','|','|','|']
    win='False'
    while win != 'IA' and win != 'J':
        if t =='j':
            Jnb=J()
            t='ia'
        elif t =='ia':
            Inb = Ia_intelligente((Jnb , Inb))
            t='j'
        win=verif_win(t)
        print(win , t )
        
    print(f"Bravo a {win} d'avoir gagné")
    if t == 'ia':
        apprentissage(Jnb , Inb )
    print([print(k) for k in choix])
#probleme a resoudre sur tout ce qui concerne le choix de la  case car prend pas la bonne valeur a reoudre 