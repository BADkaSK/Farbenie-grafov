import matplotlib.pyplot as plt
import graphtools as gt
import time
import random

# -------------------------------------
# Funkcia, ktorá získa max. nezávislú množinu z grafu rekurzívne
# -------------------------------------  
def getMIS(graph):

    if len(graph) == 0:
        return [] 
    elif len(graph) == 1:
        return list(graph.nodes) 

    graph2 = graph.copy() #pracovná kópia grafu
    
    allnodes = list(graph2.nodes) #všetky vrcholy grafu
    random.shuffle(allnodes) #náhodne preusporiadanie vrcholov

    vertexCurrent = allnodes[0] #aktuálny vrchol 
    
    #prvá možnosť -> vrchol sa nenachádza v MIS
    graph2.remove_node(vertexCurrent) 
    sol1 = getMIS(graph2) #prvé riešenie

    #druhá možnosť -> vrchol sa nachádza v MIS -> zmazanie jeho susedov
    for neighbors in graph.neighbors(vertexCurrent): 
        graph2.remove_node(neighbors) 

    sol2 = [vertexCurrent] + getMIS(graph2) #druhé riešenie
    
    return max(sol1, sol2, key=len) #vyberie sa to riešenie, ktoré obsahuje viac vrcholov 

# -------------------------------------
# Funkcia, ktorá rozdelí množinu vrcholov grafu na nezávislé množiny
# -------------------------------------  
def getMisSet(graph):
   
    graphCopy = graph.copy() #pracovná kópia grafu
    misNodes = [] #inicializacia
    
    #výpočet všetkych MIS
    while True: #cyklus, ktorý postupne nájde všetky MIS a vymaže ich z grafu
        size = len(graphCopy) #veľkosť aktuálneho grafu
        if size == 1: #MIS je samotný vrchol
            MIS = list(graphCopy.nodes)[0]
            graphCopy.remove_node(MIS) #vrchol sa zmaže
            misNodes.append([MIS]) #vrchol sa pripíše do misNodes samostatne
        elif size == 0: #našlo všetky MIS, koniec   
            break 
        else: #výpočet MIS pomocou rekurzie z akuálneho grafu
           MIS = getMIS(graphCopy) 
           graphCopy.remove_nodes_from(MIS) #MIS sa zmaže z akuálneho grafu
           misNodes.append(MIS) #MIS sa pripíše do misNodes
    
    return misNodes 

# -------------------------------------
# Hlavný program
# -------------------------------------  
def main():
       
    #menšie grafy
    #FileGraph = nx.karate_club_graph()
    #FileGraph = gt.get_bench_graph('myciel4.txt')
    #FileGraph = gt.get_bench_graph('david.txt')
    #FileGraph = gt.get_bench_graph('queen5_5.txt')
    #FileGraph = gt.get_bench_graph('queen6_6.txt')
    #FileGraph = gt.get_bench_graph('queen7_7.txt')
    #FileGraph = gt.get_bench_graph('myciel6.txt')
    #FileGraph = gt.get_bench_graph('queen9_9.txt')
    
    #malé grafy
    #FileGraph = gt.get_graph('peterson.txt')
    #FileGraph = gt.get_graph('sudoku.txt')
    #FileGraph = gt.get_graph('krizovatka.txt')
    #FileGraph = gt.get_graph('sabina.txt')
    FileGraph = gt.get_graph('random.txt')
    
    start = time.time()
    MISnodes = getMisSet(FileGraph)
    end = time.time()
    print("Čas výpočtu:") 
    print(end-start) #čas výpočtu
    
    chromNum = gt.getChrom(MISnodes) #výpis počtu použitých farieb
    print("Počet použitých farieb: ",chromNum)

    gt.drawGraph(FileGraph, MISnodes) #vykreslenie grafu
    plt.show()

# -------------------------------------
# Volanie hlavného programu
# -------------------------------------  
if __name__ == '__main__':
    main()