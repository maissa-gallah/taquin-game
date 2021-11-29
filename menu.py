from iterative import profondeur_iterative
from largeur import largeur_dabord
from profondeur import profondeur_dabord
import time
from taquin import afficher_performance

def main():
    #exemple etat intial pour 8-puzzle : 1 0 2 3 4 5 6 7 8
    print("\n\n**************** Résoudre taquin avec la recherche non informée *******************\n")
    
    type_taquin = int(input("Quel est le type du taquin (exple : 8, 15 , ...) : "))
    
    taquin_initial_sequence = input("\nQuelle est la séquence intiale du taquin ? : ")
    etat_initial = list(map(int, taquin_initial_sequence.split(" ")))
    
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

def afficher_complexites(etats_explores, noeuds_à_explorer):
    print("Complexité du temps : ",len(etats_explores))
    print("Complexité d'espace : ",len(etats_explores)+len(noeuds_à_explorer))

if __name__ == '__main__':
    main()