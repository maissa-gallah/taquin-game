from iterative import profondeur_iterative
from largeur import largeur_dabord
from profondeur import profondeur_dabord
from a import a
from taquin import afficher_performance

import time

def main():
    
    type_taquin = int(input("Quel est le dimension du taquin (exple : 3, 4 , ...) : "))
    
    taquin_initial_sequence = input("\nQuelle est la séquence intiale du taquin ? ")
    etat_initial = list(map(int, taquin_initial_sequence.split(" ")))

    print("\nQuelle est le type de recherche ? ")
    print("\n\t1/ Recherche non informé ")
    print("\t2/ Recherche informé ")

    choix_recherche = int(input("\nVotre choix : "))
    
    if choix_recherche == 1:
        print("\n\t1/ Chercher la solution avec la recherche en largeur d'abord")
        print("\t2/ Chercher la solution avec la recherche en profondeur d'abord")
        print("\t3/ Chercher la solution avec la recherche en profondeur itérative")
        print("\t4/ Comparer la performance des algorithmes")
    
        choix_algorithme = int(input("\nVotre choix : "))
    
        if choix_algorithme == 1:
            execute_algorithm_dabord(largeur_dabord,etat_initial,type_taquin)
        
        elif choix_algorithme == 2:
            execute_algorithm_dabord(profondeur_dabord,etat_initial,type_taquin)
        
        elif choix_algorithme == 3:
            execute_algorithm_iterative(profondeur_iterative, etat_initial,type_taquin)
        
        elif choix_algorithme == 4:  
            etats_explores_largeur, noeuds_à_explorer_largeur = execute_algorithm_dabord(largeur_dabord,etat_initial,type_taquin)
            etats_explores_profondeur, noeuds_à_explorer_profondeur = execute_algorithm_dabord(profondeur_dabord,etat_initial,type_taquin)
            etats_explores_iterative, noeuds_à_explorer_iterative = execute_algorithm_iterative(profondeur_iterative,etat_initial,type_taquin)
        
            print("#======================================================================================#")
            print("\n\n\tComparaison des performances :\nTime complexity (nbre de noeuds visités)\nSpace complexity (nbre max de noeuds stockés dans la mémoire = noeuds visités + noeuds à visiter)\n\n")
            print("Pour la recherche en largeur d'abord' :")
            afficher_complexites(etats_explores_largeur, noeuds_à_explorer_largeur)

            print("\nPour la recherche en profondeur d'abord :")
            afficher_complexites(etats_explores_profondeur, noeuds_à_explorer_profondeur)

            print("\nPour la recherche en profondeur itérative :")
            afficher_complexites(etats_explores_iterative, noeuds_à_explorer_iterative)
        else :
            print("mauvais choix")
            exit()
        
    elif choix_recherche == 2:

        print("\n\t1/ Chercher la solution avec la recherche A* avec h = nombre de pièces mal placées")
        print("\t2/ Chercher la solution avec la recherche A* avec h = somme des distances de chaque pièce à sa position finale")
        print("\t3/ Comparer la performance des algorithmes")
    
        choix_algorithme = int(input("\nVotre choix : "))
    
        if choix_algorithme == 1:
            a_h(a,etat_initial,type_taquin,"h1")
        
        elif choix_algorithme == 2:
            a_h(a,etat_initial,type_taquin,"h2")

        elif choix_algorithme == 3:
            etats_explores_1, noeuds_à_explorer_1 = a_h(a,etat_initial,type_taquin,"h1")
            etats_explores_2, noeuds_à_explorer_2 = a_h(a,etat_initial,type_taquin,"h2")
        
            print("#======================================================================================#")
            print("\n\n\tComparaison des performances :\nTime complexity (nbre de noeuds visités)\nSpace complexity (nbre max de noeuds stockés dans la mémoire = noeuds visités + noeuds à visiter)\n\n")
            
            print("Pour la recherche A* avec h = nombre de pièces mal placées :")
            afficher_complexites(etats_explores_1, noeuds_à_explorer_1)

            print("\nPour la recherche A* avec h = somme des distances de chaque pièce à sa position finale :")
            afficher_complexites(etats_explores_2, noeuds_à_explorer_2)

        else :
            print("mauvais choix")
            exit()

    else :
        print("mauvais choix")
        exit()
    
    
         
def execute_algorithm_dabord(algorithm,etat_initial,type_taquin):
    
    start_time = time.perf_counter()
    results = algorithm(etat_initial,type_taquin)
    end_time = time.perf_counter()
    etats_explores, noeud_final, noeuds_à_explorer = results[0],results[1], results[2]
    nbre_noeuds_visités = len(etats_explores)
    afficher_performance(etat_initial,noeud_final,nbre_noeuds_visités, start_time, end_time)
    return etats_explores,noeuds_à_explorer



def execute_algorithm_iterative(algorithm,etat_initial,type_taquin):

    noeud_final = None
    nbre_noeuds_visités = 0
    max_depth = 0
    start_time = time.perf_counter()
    while (noeud_final is None):
        results = algorithm(etat_initial,type_taquin,max_depth)
        etats_explores, noeud_final = results[0],results[1]
        nbre_noeuds_visités += len(etats_explores)
        max_depth += 1    
    end_time = time.perf_counter()
    afficher_performance(etat_initial,noeud_final,nbre_noeuds_visités, start_time, end_time)
    noeuds_à_explorer = results[2]
    return etats_explores,noeuds_à_explorer

def a_h(algorithm,etat_initial,type_taquin,h):
    
    start_time = time.perf_counter()
    results = algorithm(etat_initial,type_taquin,h)
    end_time = time.perf_counter()
    etats_explores, noeud_final, noeuds_à_explorer = results[0],results[1], results[2]
    nbre_noeuds_visités = len(etats_explores)
    afficher_performance(etat_initial,noeud_final,nbre_noeuds_visités, start_time, end_time)
    return etats_explores,noeuds_à_explorer


def afficher_complexites(etats_explores, noeuds_à_explorer):
    print("Complexité du temps : ",len(etats_explores))
    print("Complexité d'espace : ",len(etats_explores)+len(noeuds_à_explorer))

if __name__ == '__main__':
    main()