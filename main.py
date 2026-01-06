# File principale: confronto AC3 e AC4 sui sudoku

import time
from sudokus.sudokus_to_solve import *
from algorithms.CSP import stampa_sudoku_da_domini, costruisci_domini, costruisci_vicini
from algorithms.AC3 import ac3
from algorithms.AC4 import ac4

sudokus = [sudoku1, sudoku2, sudoku3, sudoku4, sudoku5]

# Faccio subito la griglia dei vicini perché tanto è indipendente dal dominio
# Contiene per ogni cella (r,c) gli elementi sulla stessa riga, colonna e blocco 3x3
vicini = costruisci_vicini()

# Il numero di archi totali per il sudoku è il numero di elementi in vicini
archi = sum(len(x) for x in vicini.values())

for i, griglia in enumerate(sudokus):
    print(f"\nSudoku numero {i + 1}")
    for riga in griglia:
        print(" ".join(riga))

    ### AC3 ###

    domini_ac3 = costruisci_domini(griglia)

    start = time.perf_counter()
    successo3, revisioni3, rimozioni3, max_coda3 = ac3(domini_ac3, vicini)
    tempo3 = time.perf_counter() - start

    celle_risolte3 = sum(1 for d in domini_ac3.values() if len(d) == 1)

    print("\nAC3")
    print("Successo:", successo3)
    print("Tempo:", round(tempo3*1000, 5), "ms")
    print("Revisioni:", revisioni3)
    print("Valori rimossi:", rimozioni3)
    print("Archi:", archi)
    print("Picco coda:", max_coda3)
    print("Celle risolte:", celle_risolte3, "/ 81")

    if celle_risolte3 == 81:
        print("\nSudoku risolto:")
        stampa_sudoku_da_domini(domini_ac3)
    else:
        print("\nSudoku non completamente risolto")

    ### AC4 ###

    domini_ac4 = costruisci_domini(griglia)

    start = time.perf_counter()
    successo4, revisioni4, rimozioni4, contatori4, supporti4, max_coda4 = ac4(domini_ac4, vicini)
    tempo4 = time.perf_counter() - start

    celle_risolte4 = sum(1 for d in domini_ac4.values() if len(d) == 1)

    print("\nAC4")
    print("Successo:", successo4)
    print("Tempo:", round(tempo4*1000, 5), "ms")
    print("Numero aggiornamenti di contatori:", revisioni4)
    print("Valori rimossi:", rimozioni4)
    print("Contatori:", contatori4)
    print("Supporti:", supporti4)
    print("Picco coda:", max_coda4)
    print("Celle risolte:", celle_risolte4, "/ 81")

    if celle_risolte4 == 81:
        print("\nSudoku risolto:")
        stampa_sudoku_da_domini(domini_ac4)
    else:
        print("\nSudoku non completamente risolto")
    print("\n----------------------------------------------")
