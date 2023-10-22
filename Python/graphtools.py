import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
import numpy as np
import randomcolor

# *************************************
# Súbor s pomocnými funkciami
# *************************************

# -------------------------------------
# Funkcia na prepočet grafu (graf začína od 1 a je nutné, aby začínal od 0)
# ------------------------------------- 
def get_bench_graph2(file): 
    list_edges = get_benchmark_edges(file)
    #prepočet vrcholov    
    list_edges2=[]
    for edge in list_edges:
        list_edges2.append([str(int(edge[0])-1),str(int(edge[1])-1)])
    FileGraph = nx.Graph() 
    FileGraph.add_edges_from(list_edges2)
    
    return FileGraph

# -------------------------------------
# Funkcia, ktorá vyfarbí kliku v grafe
# ------------------------------------- 
def cliQueColor(graph,clique): 
    otherNodes = [node for node in graph.nodes if node not in clique]
    ColoredNodes = [clique,otherNodes]
    
    generator = randomcolor.RandomColor()
    #random_colors = generator.generate(luminosity='bright', count=len(ColoredNodes)) #pastelové
    random_colors = generator.generate(luminosity='light', count=len(ColoredNodes)) #jasné
    
    result = [mcolors.hex2color(color) for color in random_colors]
  
    lenColorArray = maxNode(graph)+1
    colormap = [None]*(lenColorArray) #inicializácia colormapy pre uloženie farieb
    
    i = 0
    for COLOR in ColoredNodes:
        for node in COLOR:
            colormap[(int(node)-1)]=result[i] 
        i += 1 #posun o farbu
    
    #priradenie farieb vrcholom
    colormap2 = []
    for node in graph:
        colormap2.append(colormap[int(node)-1])
    nx.draw(graph, node_color=colormap2, with_labels=True)

# -------------------------------------
# Funkcia, ktorá vygeneruje náhodnú colormapu // môžu byť rovnaké/podobné farby
# ------------------------------------- 
def GetColormapRandom(lenColorArray, ColoredNodes, graph):
    colormap = [None]*lenColorArray #inicializácia colormapy pre uloženie farieb
    colors = np.random.random((len(ColoredNodes),3)) #náhodné farby
    result = (colors).tolist() 

    i = 0
    for COLOR in ColoredNodes:
        for node in COLOR:
            colormap[(int(node)-1)]=result[i] #vrchol na indexe dostane farbu podľa množiny
        i += 1 #posun o farbu
    
    #priradenie farieb vrcholom
    colormap2 = []
    for node in graph:
        colormap2.append(colormap[int(node)-1])
    nx.draw(graph, node_color=colormap2, with_labels=True)

# -------------------------------------
# Funkcia, ktorá vygeneruje randomcolor colormapu // farby môžu byť podobné
# ------------------------------------- 
def GetColormapRC(lenColorArray, ColoredNodes, graph): #randomcolor colormapa
    generator = randomcolor.RandomColor()
    
    random_colors = generator.generate(luminosity='bright', count=len(ColoredNodes)) #pastelové
    #random_colors = generator.generate(luminosity='light', count=len(ColoredNodes)) #jasné
    
    result = [mcolors.hex2color(color) for color in random_colors]

    colormap = [None]*lenColorArray
    i = 0
    for COLOR in ColoredNodes:
        for node in COLOR:
            colormap[(int(node)-1)]=result[i] #vrchol na indexe dostane farbu podľa množiny
        i += 1 #posun o farbu
    
    #priradenie farieb vrcholom
    colormap2 = []
    for node in graph:
        colormap2.append(colormap[int(node)-1])
    nx.draw(graph, node_color=colormap2, with_labels=True)

# -------------------------------------
# Funkcia, ktorá načíta graf zo súboru a uloží ho ako NetworkX štruktúru
# ------------------------------------- 
def get_graph(file): 
    graphFromFile = get_list_edges(file)
    FileGraph = nx.Graph() #použije knižnicu na graf
    for edges in graphFromFile:
        if len(edges) == 1:
            FileGraph.add_node(edges[0])
        else:
            FileGraph.add_edge(edges[0],edges[1])
    return FileGraph

# -------------------------------------
# Funkcia, ktorá načíta benchmark graf zo súboru a uloží ho ako NetworkX štruktúru
# ------------------------------------- 
def get_bench_graph(file): 
    graphFromFile = get_benchmark_edges(file)
    FileGraph = nx.Graph() #použije knižnicu na graf
    FileGraph.add_edges_from(graphFromFile) 
    return FileGraph

# -------------------------------------
# Funkcia, ktorá načíta riadky grafu z .txt súboru
# ------------------------------------- 
def get_list_edges(take_file):
    with open(take_file) as file:
        list_edges = []
        for line in file:
            line = line.rstrip() 
            split_values = line.split()
            list_edges.append(split_values)
        return list_edges

# -------------------------------------
# Funkcia, ktorá načíta riadky benchmark grafu z .txt súboru   
# -------------------------------------    
def get_benchmark_edges(file): 
    list_edges = []
    for line in open(file):
        if line.startswith('c') or line.startswith('p'):
            continue
        line = line.rstrip() 
        split_values = line.split()
        list_edges.append(split_values[1:3])
    return list_edges

# -------------------------------------
# Funkcia, ktorá vykreslí graf a vyfarbí vrcholy 
# -------------------------------------   
def drawGraph(graph, ColoredNodes): 
      
    lenColorArray = maxNode(graph) + 1
    GetColormapRC(lenColorArray, ColoredNodes, graph) #colormapa random color
    #GetColormapRandom(lenColorArray, ColoredNodes, graph) #colormapa náhodné farby

# -------------------------------------
# Funkcia, ktorá rozdelí list farieb do skupín podľa farieb
# ------------------------------------- 
def getGroups(colors): 
    Groups = []
 
    for i in range(max(colors)+1): 
        Nodes = []
        for node in range(len(colors)): 
            if i == colors[node]: 
                Nodes.append(node)
        Groups.append(Nodes) #nested list na uloženie skupín vrcholov podľa farieb
    return Groups

# -------------------------------------
# Funkcia, ktorá získa počet použitých farieb
# ------------------------------------- 
def getChrom(Groups):
    sumEmp = 0
    for color in Groups:
        if color == []:
            sumEmp += 1
    chromNum = len(Groups)-sumEmp
    return chromNum

# -------------------------------------
# Funkcia, ktorá nájde vrchol s najvyššou hodnotou
# -------------------------------------   
def maxNode(graph): 
    nodesList = (list(graph.nodes))
    nodes = [int(i) for i in nodesList]
    max = (nodes[np.argmax(nodes)])
    return max

# -------------------------------------
# Funkcia, ktorá nájde vrchol s najnižšou hodnotou
# -------------------------------------  
def minNode(graph):
    nodesList = (list(graph.nodes))
    nodes = [int(i) for i in nodesList]
    min = (nodes[np.argmin(nodes)])
    return min

# -------------------------------------
# Funkcia, ktorá vráti prienik dvoch listov
# -------------------------------------  
def intersection(list1, list2): 
    list3 = [value for value in list1 if value in list2]
    return list3

# -------------------------------------
# Funkcia, ktorá usporiada vrcholy podľa stupňa zostupne
# -------------------------------------  
def DescendingDegree(graph): 
    allnodes = sorted(graph.degree, key=lambda x: x[1], reverse=True)
    return [item[0] for item in allnodes]
