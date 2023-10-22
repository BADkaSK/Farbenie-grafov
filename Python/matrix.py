import networkx as nx
import graphtools as gt

# -------------------------------------
# Hlavný program
# -------------------------------------  
def main():
    
    #Vstupné grafy
    #FileGraph = gt.get_bench_graph('flat300_28_0.txt')
    #FileGraph = gt.get_bench_graph('flat1000_76_0.txt')
    FileGraph = gt.get_bench_graph('queen11_11.txt')
    #FileGraph = gt.get_bench_graph('miles1500.txt')
    #FileGraph = gt.get_bench_graph('queen5_5.txt')
    #FileGraph = gt.get_bench_graph('queen6_6.txt')
    #FileGraph = gt.get_bench_graph('queen7_7.txt')
    #FileGraph = gt.get_bench_graph('queen11_11.txt')
    #FileGraph = gt.get_bench_graph('le450_25b.txt')
    #FileGraph = gt.get_bench_graph('david.txt')
    #FileGraph = gt.get_bench_graph('queen9_9.txt')
    #FileGraph = gt.get_bench_graph('myciel4.txt')
    #FileGraph = gt.get_bench_graph('myciel6.txt')
    #FileGraph = gt.get_graph('klikatest.txt')

# -------------------------------------
# Výpočet matice susedstva s označením stĺpcov v prvom riadku, použitie pre GAMS
# -------------------------------------  
    A = [] #matica susedstva
    Arow = [] #riadkov v A
    
    size = len(FileGraph)

    for i in range(1,size+1):
        Arow = [i] #označenie stĺpca
        
        neighbors = list(nx.neighbors(FileGraph,str(i)))
        for j in range(1,size+2):
            if str(j) in neighbors or i==j:
                Arow.append(1)
            else:
                Arow.append(0)
        A.append(Arow)
        
    #uloženie matice do súboru
    file1 = open('nazovgrafuMATRIX.txt', 'w')
    for k in range (size): #riadky
        item = A[k]
        for j in range (size+1): #stĺpce
            number = item[j]
            file1.write(str(number))
            file1.write('   ')
        file1.write("\n")
    
if __name__ == '__main__':
    main()