import matplotlib.pyplot as plt
import graphtools as gt
import random
import time as time

# -------------------------------------
# Greedy algoritmus farbenia grafu 
# ------------------------------------- 
def GreedyColor(graph):

    lenColorArray = gt.maxNode(graph)+1 #nastavenie veľkosti listu colors
    
    colors = [-1]*lenColorArray #colors sa nastavi na hodnoty, ktoré nikdy nenastanú
    colors[0] = 0 #prvý vrchol bude mať prvú dostupnú farbu - 0
   
    list_of_nodes = list(graph.nodes) #list vrcholov
    
    #VÝBER HEURESTIKY RANDOM/W-P - vybrať práve jednu z nich
    
    random.shuffle(list_of_nodes) #random
    #list_of_nodes = gt.DescendingDegree(graph) #Welsh-Powell
    
    for j in range (len(list_of_nodes)): #cyklus cez všetky vrcholy
        
        available_colors = [True] * lenColorArray  #pomocný zoznam na uloženie dostupných farieb
        node = (list_of_nodes[j]) #aktuálny vrchol
        
        for i in graph.neighbors(node): #susedia aktuálneho vrcholu  
            if ((colors[int(i)]) != -1):  
                available_colors[colors[int(i)]] = False  #farba suseda sa nastaví ako nepoužiteľná
  
        cr = 0
        while cr < lenColorArray: #hľadá sa najnižšia použiteľná farba
            if (available_colors[cr]): 
                break 
            cr += 1  
        
        colors[int(node)] = cr #touto farbou sa nafarbí aktuálny vrchol

    return colors

# -------------------------------------
# Hlavný program
# -------------------------------------    
def main():
    #väčšie grafy
    #FileGraph = gt.get_bench_graph('le450_5c.txt')
    #FileGraph = gt.get_bench_graph('flat300_28_0.txt')
    FileGraph = gt.get_bench_graph('miles1500.txt')
    #FileGraph = gt.get_bench_graph('myciel7.txt')
    
    #menšie grafy
    #FileGraph = nx.karate_club_graph()
    #FileGraph = gt.get_bench_graph('myciel4.txt')
    #FileGraph = gt.get_bench_graph('queen5_5.txt')
    #FileGraph = gt.get_bench_graph('queen6_6.txt')
    #FileGraph = gt.get_bench_graph('queen7_7.txt')
    #FileGraph = gt.get_bench_graph('queen11_11.txt')
    #FileGraph = gt.get_bench_graph('queen9_9.txt')
    #FileGraph = gt.get_bench_graph2('david.txt')
    
    #malé grafy
    #FileGraph = gt.get_graph('peterson.txt')
    #FileGraph = gt.get_graph('sudoku.txt')
    #FileGraph = gt.get_graph('krizovatka.txt')
    
    start = time.time()
    colors = GreedyColor(FileGraph) #vráti list farieb, kde index predstavuje vrchol
    Groups = gt.getGroups(colors) #vráti získané nezávislé množiny
    end = time.time()
    print("Čas výpočtu:") 
    print(end-start) #čas výpočtu
    
    chromNum = gt.getChrom(Groups)
    print("Počet použitých farieb: ",chromNum) #výpis počtu farieb
    
    gt.drawGraph(FileGraph, Groups) #vykreslenie grafu
    plt.show() 
    

# -------------------------------------
# Volanie hlavného programu
# -------------------------------------  
if __name__ == '__main__':
    main()
