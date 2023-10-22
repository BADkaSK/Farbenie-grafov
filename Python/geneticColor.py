from array import *
import random
import matplotlib.pyplot as plt
import graphtools as gt
import time
import math

#globálne premenné
popSize = 200
selectionSize = 100
maxIT = 300
test = True
MAX_FITNESS_VAL = math.inf

# -------------------------------------
# Funkcia, ktorá odhadne chrom. číslo, v tomto prípade zoberie polovicu z hornej hranice
# ------------------------------------- 
def chromTest(graph):
    return getUpperBound(graph)//2

# -------------------------------------
# Funkcia, ktorá zistí hornú hranicu chrom. čísla podľa Brooksovej vety
# -------------------------------------
def getUpperBound(graph): 
    nodes = gt.DescendingDegree(graph)
    degreeMax = graph.degree[nodes[0]]
    return degreeMax + 1

# -------------------------------------
# Funkcia, ktorá vypočíta fitness hodnotu pre dané farbenie
# vráti 0, keď je farbenie uskutočniteľné
# -------------------------------------
def fitnessEval(graph, individual): 
    fitness = 0
    n = len(graph)
    for i in range(n):
        for j in range(i, n):
            neighbors = graph.neighbors(str(i)) 
            if(individual[i] == individual[j] and (str(j) in neighbors)):
                fitness += 1
    return fitness

# -------------------------------------
# Funkcia, ktorá simuluje párenie jedincov/farbení grafu -> výstup 2 novi jedinci
# -------------------------------------
def crossover(graph, parent1, parent2):
    position = random.randint(2, len(graph)-2) #náhodný crossover bod
    child1 = []
    child2 = []
    for i in range(position+1):
        child1.append(parent1[i])
        child2.append(parent2[i])
    for i in range(position+1, len(graph)):
        child1.append(parent2[i])
        child2.append(parent1[i])
    return child1, child2

# -------------------------------------
# Funkcia, ktorá simuluje mutáciu verzia 1
# -------------------------------------       
def mutation1(individual, k, n): #prvý typ mutácie
    probability = 0.3
    check = random.uniform(0, 1)
    if(check <= probability):
        position = random.randint(0, n-1)
        individual[position] = random.randint(1, k)
    return individual

# -------------------------------------
# Funkcia, ktorá simuluje mutáciu verzia 2
# -------------------------------------   
def mutation2(individual, number_of_colors, n): #druhý typ mutácie
    probability = 0.2
    check = random.uniform(0, 1)
    if(check <= probability):
        position = random.randint(0, n-1)
        individual[position] = random.randint(1, number_of_colors)
    return individual

# -------------------------------------
# Funkcia ruletovej selekcie populácie
# -------------------------------------   
def rouletteSelections(graph, population): 
    global selectionSize
    
    #normalizované hodnoty fitness
    fitnessSum = sum([1/(1+fitnessEval(graph, individual)) for individual in population])
    
    rouletteVal = []
    rouletteSum = 0
    
    for i in range(len(population)): #hodnoty ruletového kolesa
        #nižšie hodnoty fitness získaju väčšiu časť
        rouletteSum += 1 / (1+fitnessEval(graph, population[i]))/fitnessSum 
        rouletteVal.append(rouletteSum) #pridelenie časti kolesa

    new_population = []
    for i in range (selectionSize):
        roulette = random.uniform(0, 1) #simulácia roztočenia rulety
        for j in range(len(population)):
            if (roulette <= rouletteVal[j]):
                new_population.append(population[j])
                break
    return new_population

# -------------------------------------
# Funkcia výpočtu nového jedinca/farbenia grafu
# -------------------------------------    
def newInd(k, n):
    individual = [random.randint(1, k) for l in range(n)] #náhodné farbenie
    itLoop = 10 #počet pokusov
    
    for i in range(itLoop): #generovanie jedincov náhodne, aby obsahovali všetky farby
        missColor = False
        for j in range(1,k+1):
            if j not in individual: #nejaká farba chýba vo farbení
                missColor = True          
                break
        if missColor: #jedinec sa vygeneruje znova
            individual = [random.randint(1, k) for l in range(n)] #náhodné farbenie
        else:
            break
    
    if i > itLoop and missColor:
        print("Nepodarilo sa vygenerovať individuála na ",itLoop," iterácii")  
          
    return individual

# -------------------------------------
# Funkcia vytvorenia prvej populácie
# -------------------------------------        
def initPop(k, n): #inicializácia populácie
    global popSize
    population = [newInd(k, n) for i in range(popSize)]
    return population

# -------------------------------------
# Genetický algoritmus farbenia grafu
# -------------------------------------  
def GeneticColoring(graph,max_num_colors,test_number):
    global popSize, selectionSize, maxIT
    
    k = test_number
    validity = False
    bestInd  = {0}

    while(k > 0): 

        population = initPop(k, len(graph))
        bestFitness = MAX_FITNESS_VAL #nedosiahnuteľná hodnota
        betterInd = population[0]
        gen = 0
    
        while(bestFitness != 0 and gen != maxIT): #cyklus kým sa nenašlo uskutočniteľné farbenie 
            
            gen += 1 #posun na novú generáciu
            population = rouletteSelections(graph, population) #selekcia
            newPop = []
            random.shuffle(population) #náhodné premiešanie populácie
            
            for i in range(0, selectionSize-1, 2): 
                
                child1, child2 = crossover(graph, population[i], population[i+1])
                newPop.append(child1) #1 nový jedinec sa pridá do populácie
                newPop.append(child2) #2 nový jedinec sa pridá do populácie
                
            for individual in newPop: #mutácia
                if(gen < 200):
                    individual = mutation1(individual, k, len(graph))
                else:
                    individual = mutation2(individual, k, len(graph))
            
            population = newPop
            
            #získanie jedinca s najlepšou hodnotou fitness
            bestFitness = MAX_FITNESS_VAL 

            betterInd = population[0]
            for individual in population:
                fitval = fitnessEval(graph, individual)
                if( fitval < bestFitness):
                    bestFitness = fitval
                    betterInd = individual
                    if(bestFitness == 0): #našlo sa uskutočniteľné k-farbenie
                        bestInd = betterInd  
                        validity = True 
                        break #ďalej sa nemusí počítať
                            
        #výpis pre každé k-farbenie            
        print("Počet farieb", k)
        print("Generácia: ", gen)
        print("Najlepšia hodnota fitness: ", bestFitness)
        print("Najlepší jedinec: ", betterInd)

        if(bestFitness != 0): 
            break #koniec výpočtu
        else:
            k -= 1 #zníženie počtu farieb

    print("Validita: " , validity , " Najlepšie farbenie: ", bestInd)
   
    return validity,bestInd

# -------------------------------------
# Hlavný program
# ------------------------------------- 
def main():
    
    #FileGraph = nx.karate_club_graph()
    
    #menšie grafy
    #len na testovacie účely - prepočíta graf
    #FileGraph = gt.get_bench_graph2('queen9_9.txt')
    #FileGraph = gt.get_bench_graph2('david.txt') 
    #FileGraph = gt.get_bench_graph2('myciel4.txt')
    #FileGraph = gt.get_bench_graph2('myciel6.txt')
    #FileGraph = gt.get_bench_graph2('queen5_5.txt')
    #FileGraph = gt.get_bench_graph2('queen6_6.txt')
    #FileGraph = gt.get_bench_graph2('queen7_7.txt')
    #FileGraph = gt.get_bench_graph2('queen9_9.txt')
    
    #malé grafy
    #FileGraph = gt.get_graph('peterson.txt')
    #FileGraph = gt.get_graph('sudoku.txt')
    FileGraph = gt.get_graph('sabina.txt')
    #FileGraph = gt.get_graph('random.txt')
    #FileGraph = gt.get_graph('bip.txt')
    
    max_number_colors = getUpperBound(FileGraph) 
    test_number = chromTest(FileGraph)        
    
    start = time.time()
    valid,color = GeneticColoring(FileGraph, max_number_colors,test_number) #prvé otestovanie polovice hornej hranice
    
    if not valid: #test nevyšiel -> výpočet znova pre hornú hranicu chrom. čísla
        valid,color = GeneticColoring(FileGraph, max_number_colors, max_number_colors)
    end = time.time()
    print("Čas výpočtu:") 
    print(end-start) #čas výpočtu
 
    if valid:
        Groups = gt.getGroups(color)
        chromNum = gt.getChrom(Groups)
        print("Počet použitých farieb: ",chromNum)
        gt.drawGraph(FileGraph, Groups)
        plt.show()
    else:
        print("Neplatné farbenie")

    print("Koniec výpočtu")
 
# -------------------------------------
# Volanie hlavného programu
# -------------------------------------  
if __name__ == '__main__':
    main()
        