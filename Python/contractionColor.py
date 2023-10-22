import networkx as nx
import matplotlib.pyplot as plt
import graphtools as gt
import time

# -------------------------------------
# Funkcia kontroly úplnosti grafu
# ------------------------------------- 
def isCompleted(graph): 
    n = len(graph) #počet vrcholov
    max_edges = n*(n-1)/2 #počet hrán uplného grafu s n vrcholmi
    if nx.number_of_edges(graph) == max_edges:
        return True #graf je úplný
    else:
        return False #graf nie je úplný

# -------------------------------------
# Funkcia, ktorá označí a uchová spracovanie vrcholu v tabuľke 
# ------------------------------------- 
def SetNodePocessed(index, val, table):

    if index < len(table):
        table[index] = val
    return 

# -------------------------------------
# Funkcia, ktorá vyberie ešte nespracovaný vrchol na spracovanie
# ------------------------------------- 
def GetNextUnprocessedNod(nodes, table): 

    for node in nodes: #cyklus cez všetky vrcholy
        numNode = int(node) #z char sa vytvorí index v tabuľke
        if numNode < len(table):           
            if table[numNode] == False : #vyberie sa prvý nespracovaný vrchol
                SetNodePocessed(numNode,True,table) #označí sa ako spracovaný
                return node
    return 'Nothing' #všetky vrcholy spracované

# -------------------------------------
# Zlepovací algoritmus farbenia grafu
# ------------------------------------- 
def ContractionColor(graph):
    graphCopy = graph.copy() #pracovná kópia grafu

    dispatchModeTable = [False]*(gt.maxNode(graph)+1) #inicializácia tabuľky

    connections = []*len(graphCopy) #inicializácia listu zlepených vrcholov
    allnodes = gt.DescendingDegree(graphCopy) #vrcholy sa usporiadajú zostupne podľa stupňa

    while True :  

        node = GetNextUnprocessedNod(allnodes,dispatchModeTable) #aktuálny vrchol
        if node == 'Nothing': #všetky vrcholy sú spracované
            break
        
        con = [] #pomocný list pre zápis
        con.append(node) #vloženie vrcholu do listu

        if(len(list(nx.non_neighbors(graphCopy,node)))) != 0: #kontrola, či má vrchol má nesusedov

            nonNeighbor = 'init' #inicializačná hodnota 
            while(nonNeighbor != 'Nothing'): #cyklus, pokiaľ má vrchol nesusedov

                #inicializácie
                nonNeighbor = 'Nothing' 
                commonNeighbors = []

                #výber najvhodnejšieho nesuseda - vyberie sa nesused s najviac spol. susedmi
                max = 0
                for nonNeighbor in nx.non_neighbors(graphCopy,node): 
                    commonNeighbors = list(nx.common_neighbors(graphCopy, node, nonNeighbor))
                    if len(commonNeighbors) > max:
                        max = len(commonNeighbors)
                        best = nonNeighbor
               
                if max == 0 & len(commonNeighbors) == 0: #prípad, že vrchol má nesusedov, ale nemá s nimi spol. susedov
                    best = nonNeighbor         
                            
                if nonNeighbor == 'Nothing': #prípad, že nie sú žiadni nesusedia
                    break #presun na ďalší vrchol
                
                else: #bol vybratý najvhodnejší nesused a nasleduje kontrakcia vrcholov (zlepenie)
                    bestNeighbors = list(nx.neighbors(graphCopy,best)) #susedia vrcholu best
                    
                    #zjednotenie susedov
                    for neighbor in bestNeighbors:
                        graphCopy.add_edge(node, neighbor) 
                    
                    graphCopy.remove_node(best) #zmazanie best
                    allnodes = gt.DescendingDegree(graphCopy) #vrcholy sa znova usporiadajú po vymazaní best
                            
                    con.append(best) #pridanie best do listu connections
                
        connections.append(con)
        
    if isCompleted(graphCopy): #graf je úplný - koniec                                                                                    
        return True, connections
    else: #v prípade, že graf z nejakého neznámeho dôvodu nie je úplný
        return False

# -------------------------------------
# Hlavný program
# -------------------------------------        
def main():
    
    #väčšie grafy
    FileGraph = gt.get_bench_graph('le450_5c.txt')
    #FileGraph = gt.get_bench_graph('flat300_28_0.txt')
    #FileGraph = gt.get_bench_graph('miles1500.txt')
    #FileGraph = gt.get_bench_graph('myciel7.txt')
    #FileGraph = gt.get_bench_graph('queen11_11.txt')
    
    #menšie grafy
    #FileGraph = nx.karate_club_graph()
    #FileGraph = gt.get_bench_graph('myciel4.txt')
    #FileGraph = gt.get_bench_graph('queen5_5.txt')
    #FileGraph = gt.get_bench_graph('queen6_6.txt')
    #FileGraph = gt.get_bench_graph('queen7_7.txt')
    #FileGraph = gt.get_bench_graph('queen9_9.txt')
    #FileGraph = gt.get_bench_graph('david.txt')
    
    #malé grafy
    #FileGraph = gt.get_graph('peterson.txt')
    #FileGraph = gt.get_graph('sudoku.txt')
    #FileGraph = gt.get_graph('random.txt')
    #FileGraph = gt.get_graph('krizovatka.txt')
    #FileGraph = gt.get_graph('random.txt')
    
    start = time.time()
    result = ContractionColor(FileGraph) #vráti získané nezávislé množiny
    end = time.time()
    print("Čas výpočtu:") 
    print(end-start) #čas výpočtu
    
    if (result)[0]:
        chromNum = gt.getChrom((result)[1])
        print("Počet použitých farieb: ",chromNum) #výpis počtu farieb
        
        gt.drawGraph(FileGraph, (result)[1]) #vykreslenie
        plt.show() 

    else:
        print("Nepodarilo sa nafarbiť graf")
                  
# -------------------------------------
# Volanie hlavného programu
# ------------------------------------- 
if __name__ == '__main__':
    main()
