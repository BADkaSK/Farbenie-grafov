import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import graphtools as gt
import random
import time
NOT_DEF_COLOR = -1

# -------------------------------------
# Funkcia, ktorá aktualizuje hodnoty saturácie vrcholov - počet rôzne ofarbených susedných vrcholov
# -------------------------------------  
def Satur(graph,colors,list_of_nodes,nodeActual,sat):
    
    neighborsColor = []
     
    neighborsNode = gt.intersection(list(nx.neighbors(graph,nodeActual)),list_of_nodes) #susedia akt. vrcholu
    
    #aktualizuje sa saturácia všetkých susedov akt. vrcholu
    for node in neighborsNode:
        neighbors = list(nx.neighbors(graph,node)) #susedia susedov akt. vrcholu
        for neighbor in neighbors:
            if colors[int(neighbor)] != NOT_DEF_COLOR: #
                neighborsColor.append(colors[int(neighbor)]) #nájde list farieb susedov 
        
        counts = np.unique(neighborsColor) #nájde počet rôznych farieb u susedov
        sat[int(node)] = len(counts) #výpočet saturácie vrcholu
      
        neighborsColor = []

    return sat 


# -------------------------------------
# Greedy algoritmus s heuristikou DSatur farbenia grafu
# -------------------------------------     
def GreedyColor(graph):
    
    lenColorArray = gt.maxNode(graph)+1 #nastavenie veľkosti listu colors
    minNode = gt.minNode(graph)
    
    colors = [NOT_DEF_COLOR]*lenColorArray #colors sa nastaví na hodnoty, ktoré nikdy nenastanú

    list_of_nodes = list(graph.nodes) #list vrcholov
    sat = [0]*lenColorArray #inicializácia poľa saturácie
    sat[:minNode]=[NOT_DEF_COLOR]

    #prvý vrchol sa vyberie náhodne
    node = int(random.choice(list_of_nodes))
    
    while(True): 

        list_of_nodes.remove(str(node)) #vymazanie už spracovaného vrcholu
        sat[node] = -1 #vrchol označený ako nedostupný na ďalšie farbenie
        
        available_colors = [True] * lenColorArray #pomocné pole na uloženie dostupných farieb
        
        for neighbor in nx.neighbors(graph,str(node)):  #susedia aktuálneho vrcholu  
            if ((colors[int(neighbor)]) != NOT_DEF_COLOR): 
                available_colors[colors[int(neighbor)]] = False #farba suseda sa nastaví ako nepoužitelná
  
        cr = 0
        while cr < lenColorArray: #hľadá sa najnižšia použiteľná farba  
            if (available_colors[cr]): 
                break                   
            cr += 1  
 
        colors[(node)] = cr #touto farbou sa nafarbí aktuálny vrchol
        
        if len(list_of_nodes)==0:
            break        

        else:
            #výber vrcholu
            sat = Satur(graph,colors,list_of_nodes,str(node),sat)
            node = np.argmax(sat) #vyberie sa vrchol s max saturáciou

    return colors

# -------------------------------------
# Hlavný program
# -------------------------------------  
def main():

    #väčšie grafy
    #FileGraph = gt.get_bench_graph('le450_5c.txt')
    #FileGraph = gt.get_bench_graph('flat300_28_0.txt')
    #FileGraph = gt.get_bench_graph('miles1500.txt')
    #FileGraph = gt.get_bench_graph('myciel7.txt')
    
    #menšie grafy
    #FileGraph = nx.karate_club_graph()
    FileGraph = gt.get_bench_graph('myciel4.txt')
    #FileGraph = gt.get_bench_graph('queen5_5.txt')
    #FileGraph = gt.get_bench_graph('queen6_6.txt')
    #FileGraph = gt.get_bench_graph('queen7_7.txt')
    #FileGraph = gt.get_bench_graph('queen11_11.txt')
    #FileGraph = gt.get_bench_graph('queen9_9.txt')
    #FileGraph = gt.get_bench_graph('david.txt')
    
    #malé grafy
    #FileGraph = gt.get_graph('peterson.txt')
    #FileGraph = gt.get_graph('sudoku.txt')
    #FileGraph = gt.get_bench_graph('myciel4.txt')
    #FileGraph = gt.get_graph('krizovatka.txt')
    #FileGraph = gt.get_graph('random.txt')
    
    start = time.time()
    color = GreedyColor(FileGraph) #vráti list farieb, kde index predstavuje vrchol
    Groups = gt.getGroups(color) #vráti získané nezávislé množiny
    end = time.time()
    print("Čas výpočtu:") 
    print(end-start) #čas výpočtu
    
    chromNum = gt.getChrom(Groups)
    print("Počet použitých farieb: ",chromNum) #výpis počet použitých farieb
    gt.drawGraph(FileGraph, Groups) #vykreslenie
    plt.show() 
    
# -------------------------------------
# Volanie hlavného programu
# -------------------------------------  
if __name__ == '__main__':
    main()
