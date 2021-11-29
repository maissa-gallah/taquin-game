from taquin import Jeu_Taquin,sous_noeuds


def profondeur_iterative(etat_debut,n, max_depth):
    etat_final = []
    for i in range(0,n+1):
        etat_final.append(i)
        
    etats_explores = []

    noeuds_à_explorer = list([Jeu_Taquin(etat=etat_debut,n=n)]) 

    while noeuds_à_explorer:
        noeud = noeuds_à_explorer.pop()
        
        etats_explores.append(noeud.etat)
        
        #afficher(noeud)
        
        if noeud.etat == etat_final: 
            noeud_final = noeud
            return [etats_explores, noeud_final,noeuds_à_explorer]
        
        if noeud.depth == max_depth:
            continue
        
        possibles = list(reversed(sous_noeuds(noeud)))
        for pos in possibles:
            if (pos.etat not in etats_explores) and (pos not in noeuds_à_explorer):
                noeuds_à_explorer.append(pos)
        
    return [etats_explores,None,noeuds_à_explorer]