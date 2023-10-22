Tento priečinok obsahuje programy spustiteľné v Pythone:
*****************************************
Algoritmy farbenia grafu:
greedyColor.py  	- Greedy algoritmus s heuristikami Random a Welsh-Powell
greedyDSaturColor.py	- Greedy algoritmus s heuristikou DSatur
recursiveMIS.py		- Rekurzívny algoritmus farbenia pomocou MIS
contractionColor.py	- Zlepovací algoritmus
geneticColor.py		- Genetický algoritmus
m-Color.py		- Algoritmus m-farbenia grafu 

Pomocné programy:
density.py 		- vypočíta hustotu grafu
matrix.py		- vypočíta maticu susedstva, pre vstup do GAMS programov

Pomocné funkcie:
graphtools.py		- súbor pomocných funkcií na prácu s grafom, načítanie a vykreslenie grafu

Algoritmy maximálnej kliky v grafe:
BK_clique.py 		- Bron-Kerbosh algoritmus 
BKheures_clique.py 	- Bron-Kerbosh algoritmus s výberom pivotu a degeneracy poradím

*****************************************
Vstupné hodnoty:
grafy reprezentované zoznamom hrán v textových súboroch
v ZOZNAM_GRAFOV.txt sú popísané konkrétne vstupné grafy
*****************************************
Výstupné hodnoty:
Čas výpočtu
Počet použitých farieb/ alebo Vrcholy maximálnej kliky
Vykreslenie grafu s vyfarbením - farby môžu byť podobné
*****************************************
Spustenie:
Pred spustením týchto Python skriptov musia byť nainštalované
knižnice uvedené v súbore poetry.lock alebo pomocou pip inštalátora:

Inštalácia knižníc pomocou pip:
pip install numpy
pip install matplotlib
pip install networkx
pip install randomcolor

Verzie:
Interpreter: Python: 3.11
Knižnice:
numpy: 1.24.3
matplotlib: 3.7.1
networkx: 3.1
randomcolor: 0.4.4.6