import networkx as nx
import graphtools as gt

# -------------------------------------
# Hlavný program na zistenie hustoty grafu cez knižnicu NX
# -------------------------------------  
def main():
    #FileGraph = gt.get_bench_graph('flat300_28_0.txt')
    #FileGraph = gt.get_bench_graph('flat1000_76_0.txt')
    #FileGraph = gt.get_bench_graph('myciel7.txt')
    #FileGraph = gt.get_bench_graph('miles1500.txt')
    #FileGraph = gt.get_bench_graph('queen5_5.txt')
    #FileGraph = gt.get_bench_graph('queen6_6.txt')
    #FileGraph = gt.get_bench_graph('queen7_7.txt')
    #FileGraph = gt.get_bench_graph('queen9_9.txt')
    #FileGraph = gt.get_bench_graph('queen11_11.txt')
    #FileGraph = gt.get_bench_graph('queen11_11.txt')
    FileGraph = gt.get_bench_graph('le450_25b.txt')
     
    #výpis hustoty grafu
    density = nx.density(FileGraph)
    print("Graf ma hustotu",density)

# -------------------------------------
# Volanie hlavného programu
# -------------------------------------           
if __name__ == '__main__':
    main()