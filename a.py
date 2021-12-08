from collections import deque
from taquin import Jeu_Taquin,sous_noeuds,afficher

#nb de pièces mal placées
def h1(noeud):
    n = noeud.n
    correct_pos = []
    for i in range(0,n*n):
        correct_pos.append(i)

    return sum((noeud.etat[i] != correct_pos[i]) and ( noeud.etat[i]!=0 ) for i in range(0,n*n))


#somme des distances de chaque pièce à sa position finale
def h2(noeud):
    n = noeud.n
    correct_pos = []
    for i in range(0,n*n):
        correct_pos.append(i)

    h = 0
    for i in range(0,n*n):
        if noeud.etat[i] != 0:
            h  = h + abs(correct_pos.index(noeud.etat[i]) - i )
    return h
        

    

def g(noeud):
    return noeud.depth

def f(noeud,h):
    return g(noeud) + h(noeud)

def a(etat_debut,n, type):

    if type == "h1":
        h =h1
    else:
        h = h2

    etat_final = []
    for i in range(0,n*n):
        etat_final.append(i)
        
    etats_explores = []

    noeuds_à_explorer = list([Jeu_Taquin(etat=etat_debut,n=n)]) 

    while noeuds_à_explorer:
        noeud = noeuds_à_explorer.pop()

        etats_explores.append(noeud.etat)
        
        if h(noeud) == 0: 
            noeud_final = noeud
            return [etats_explores, noeud_final,noeuds_à_explorer]

        possibles = sous_noeuds(noeud)
        for pos in possibles:
            if (pos.etat not in etats_explores) and (pos not in noeuds_à_explorer):
                pos.fval = f(pos,h)
                noeuds_à_explorer.append(pos)
        
        noeuds_à_explorer.sort(key = lambda x:x.fval,reverse=True)


def main():

    n = 3

    etat_initial =   [1,4,2,3,0,5,6,7,8]

    results = a(etat_initial,n)

    etats_explores, noeud_final, noeuds_à_explorer = results[0],results[1], results[2]

    nbre_noeuds_visités = len(etats_explores)

    
    noeud = noeud_final
    chemin_solution = [noeud_final]
    while noeud.etat != etat_initial:
        noeud = noeud.parent
        chemin_solution.append(noeud)
        
    print("Le chemin de la solution est :")
    for noeud in reversed(chemin_solution):
        afficher(noeud)
    print("Nombre totale des noeuds visités: ", nbre_noeuds_visités)
    print("La profondeur de recherche ou on a trouvé la solution: ", noeud_final.depth)


if __name__ == '__main__':
    main()