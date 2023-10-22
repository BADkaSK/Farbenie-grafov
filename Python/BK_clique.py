import matplotlib.pyplot as plt
import graphtools as gt
import networkx as nx
import time

# -------------------------------------
# Algorimus Bron-Kerbosh na výpočet všetkých maximálnych klík
# -------------------------------------
def bron_kerbosch(graph):
    cliquesSET = [] #zoznam maximálnych klík grafu
    
    #P - množina possible candidates
    #R - množina temporary result
    #X - množina vrcholov, ktoré nebudú obsiahnuté v klike
    
    def cliques(R, P, X):

        if not P and not X: #našla sa klika
            cliquesSET.append(R) #pridanie do množiny maximálnych klík a ukončenie výpočtu
            return
        
        for node in P.copy(): #cyklus pre všetky vrcholy
            neighbors = list(nx.neighbors(graph,node)) #výber susedov vrcholu
            cliques(R.union({node}), P.intersection(neighbors), X.intersection(neighbors))
            P.remove(node) #vrchol sa zmaže z P
            X.add(node) #vrchol sa pridá do X
    
    cliques(set(), set(graph.nodes()), set()) #prvé zavolanie
    return cliquesSET 

# -------------------------------------
# Hlavný program
# -------------------------------------
def main(): 
    
    #väčšie grafy
    #FileGraph = gt.get_bench_graph('le450_5c.txt')
    #FileGraph = gt.get_bench_graph('flat300_28_0.txt')
    #FileGraph = gt.get_bench_graph('myciel7.txt')
    
    #menšie grafy
    #FileGraph = nx.karate_club_graph()
    #FileGraph = gt.get_bench_graph('myciel4.txt')
    #FileGraph = gt.get_bench_graph('queen5_5.txt')
    #FileGraph = gt.get_bench_graph('queen6_6.txt')
    FileGraph = gt.get_bench_graph('queen7_7.txt')
    #FileGraph = gt.get_bench_graph('queen11_11.txt')
    #FileGraph = gt.get_bench_graph('queen9_9.txt')
    
    #malé grafy
    #FileGraph = gt.get_graph('peterson.txt')
    #FileGraph = gt.get_graph('sudoku.txt')
    #FileGraph = gt.get_graph('krizovatka.txt')
    
    start = time.time()
    BKkliky = bron_kerbosch(FileGraph) #nájde max kliky v grafe
    end = time.time()
    print("Čas výpočtu:") 
    print(end-start) #čas výpočtu
    
    maxClique = max(BKkliky, key=len) #vyberie sa klika s najväčším počtom vrcholov
    sumBK = len(BKkliky) #počet nájdených klík
    print("B-K našiel ",sumBK," klík")
    print("Vrcholy max kliky: ",maxClique) 

    ############### NetworX algoritmus na overenie ###############
    sumN = sum(1 for c in nx.find_cliques(FileGraph))  #počet max klík
    cliquesN = max(nx.find_cliques(FileGraph), key=len)  #max klika s najväčším počtom vrcholov (môže ich byť viac)
    print("NetworX našiel ",sumN," klík")
    print("Vrcholy max kliky: ",cliquesN)
    
    gt.cliQueColor(FileGraph,maxClique) #vykreslenie kliky v grafe
    plt.show()      

# -------------------------------------
# Volanie hlavného programu
# -------------------------------------    
if __name__ == "__main__":
    main()