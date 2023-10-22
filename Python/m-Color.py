import graphtools as gt
import networkx as nx
import matplotlib.pyplot as plt
import time

# -------------------------------------
# Funkcia, ktorá kontroluje kolízie farieb so susednými vrcholmi
# ------------------------------------- 
def isSafe(node, graph, color, c):
    
    for neighbor in nx.neighbors(graph,str(node)):
        if color[int(neighbor)] == c:
            return False #susedný vrchol už má priradenú farbu c
    return True #vrcholu sa môže priradiť farba c 

# -------------------------------------
# Funkcia backtracking farbenia
# ------------------------------------- 
def backtracking(graph, m, color, v, firstNode): 
    if v == len(graph) + firstNode:
        return True

    for c in range(1, m+1):
        if isSafe(v, graph, color, c): #kontrola 
            color[v] = c #vrchol môže mať farbu c
            if backtracking(graph, m, color, v+1, firstNode):
                return True 
            color[v] = 0 

    return False

# -------------------------------------
# Hlavná funkcia backtracking farbenia
# ------------------------------------- 
def backtrackColor(graph, m):
    
    allnodes = list(graph.nodes)
    firstNode = int(min(allnodes)) #nájdi najmenší vrchol:
    color = [0] * (len(graph) + (firstNode))
    if backtracking(graph, m, color, firstNode, firstNode):
        return color #farbenie bolo úspešné
    return None #farbenie bolo neúspešné
    
# -------------------------------------
# Hlavný program
# -------------------------------------   
def main():
    #FileGraph = gt.get_graph('peterson.txt')
    #m=3 #počet farieb
    
    #FileGraph = gt.get_graph('random.txt')
    #m=7 #počet farieb
    
    FileGraph = gt.get_bench_graph('myciel4.txt')
    m=5 #počet farieb
    
    #FileGraph = gt.get_bench_graph('queen5_5.txt')
    #m=5 #počet farieb
    
    #FileGraph = gt.get_bench_graph('queen6_6.txt')
    #m=7 #počet farieb
    
    start = time.time()
    colors = backtrackColor(FileGraph,m)
    
    if colors != None:
        #print(colors)
        Groups = gt.getGroups(colors) #vygeneruje zo zoznamu farieb skupiny vrcholov 
        end = time.time()
        print("Podarilo sa nafarbiť graf ",m," farbami")
        print("Čas výpočtu:") 
        print(end-start) #čas výpočtu
        gt.drawGraph(FileGraph, Groups) #vykreslenie grafu
        plt.show()
        
    else:
        print("Nepodarilo sa nafarbiť graf ",m," farbami")
        end = time.time()
    
# -------------------------------------
# Volanie hlavného programu
# -------------------------------------  
if __name__ == '__main__':
    main()
    