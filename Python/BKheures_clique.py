import matplotlib.pyplot as plt
import graphtools as gt
import networkx as nx
import time

# -------------------------------------
# Algorimus Bron-Kerbosh s heuristikami na výpočet všetkých maximálnych klík
# -------------------------------------
def cliques(graph):
  
    P = set(graph.nodes) #množina possible candidates
    R = set() #množina temporary result
    X = set() #množina vrcholov, ktoré nebudú obsiahnuté v klike

    cliquesSET = [] #zoznam maximálnych klík grafu

    for node in degenOrdering(graph): #cyklus cez usporiadané vrcholy - degeneracy ordering
        neighbors = list(nx.neighbors(graph,node)) #výber susedov akt. vrcholu
        #výber pivota 
        pivot(graph, R.union([node]), P.intersection(neighbors), X.intersection(neighbors), cliquesSET)
        #akt. vrchol sa presunie z P do X
        P.remove(node) 
        X.add(node) 
    return sorted(cliquesSET, key = lambda x: len(x), reverse=True) #výstup sa zostupne usporiada

# -------------------------------------
# Funkcia hľadania kliky s použitím výberu pivotu
# -------------------------------------
def pivot(graph, R, P, X, cliquesSET): 

    if not P and not X: #našla sa klika
        cliquesSET.append(R) #pridanie do množiny maximálnych klík a ukončenie výpočtu
    else: #nenašla sa klika
        u = next(iter(P.union(X))) #výber - ďalší vrchol na spracovanie
        Pdif = P.difference(list(nx.neighbors(graph,u))) #z P sa odstráni u a jeho susedia
        for node in Pdif: #cyklus pre vrcholy v Pdif
            neighbors = list(nx.neighbors(graph,node)) #výber susedov akt. vrcholu
            pivot(graph, R.union([node]), P.intersection(neighbors), X.intersection(neighbors), cliquesSET) #rekurzia
            #vrchol sa presunie z P do X
            P.remove(node)
            X.add(node)

# -------------------------------------
# Funkcia usporiadania vrcholov podľa degenerácie
# -------------------------------------
def degenOrdering(graph): 
    graphCopy = graph.copy() #pracovná kópia grafu
    ordering_set = [] #inicializácia 
    
    nodes = sorted(graphCopy.degree, key=lambda x: x[1], reverse=False) #zoradenie podľa stupňa vzostupne
   
    while len(nodes)>0: 
        min = nodes[0] #nájdený vrchol s najmenším stupňom
        graphCopy.remove_node(min[0]) #zmazanie vrcholu, min=[vrchol,stupeň]
        ordering_set.append(min[0]) #uloženie vrcholu do poradia
        nodes = sorted(graphCopy.degree, key=lambda x: x[1], reverse=False) #preusporiadanie

    ordering_set.reverse() #preusporiadanie
    
    return ordering_set
  
# -------------------------------------
# Hlavný program
# -------------------------------------
def main():
    
    #väčšie grafy
    #FileGraph = gt.get_bench_graph('flat300_28_0.txt')
    #FileGraph = gt.get_bench_graph('queen11_11.txt')
    
    #menšie grafy
    #FileGraph = gt.get_graph('peterson.txt')
    FileGraph = nx.karate_club_graph()
    #FileGraph = gt.get_bench_graph('myciel3.txt')
    #FileGraph = gt.get_bench_graph('myciel4.txt')
    #FileGraph = gt.get_bench_graph('queen5_5.txt')
    #FileGraph = gt.get_bench_graph('queen6_6.txt')
    #FileGraph = gt.get_bench_graph('queen7_7.txt')
    #FileGraph = gt.get_bench_graph('queen9_9.txt') 
    #FileGraph = gt.get_graph('krizovatka.txt')
    #FileGraph = gt.get_graph('klikatest.txt')
    
    ###############  PREVOD PROBLEMU NA MIS  ###############
    #FileGraphcompl = nx.complement(FileGraph) 
    ########################################################
    
    start = time.time()
    BKkliky = cliques(FileGraph) #nájde všetky max kliky v grafe
    end = time.time()
    print("Čas výpočtu:") 
    print(end-start) #čas výpočtu

    maxClique = max(BKkliky, key=len) #klika s najväčším počtom vrcholov
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