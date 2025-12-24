# File principale: confronto AC3 sui sudoku

import time
from sudokus.to_solve.sudokus_to_solve import *
from algorithms.CSP import *
from algorithms.AC3 import *

sudokus = [sudoku1, sudoku2, sudoku3, sudoku4, sudoku5]

vicini = costruisci_vicini()

for i, griglia in enumerate(sudokus):
    print(f"\nSudoku {i + 1}")

    domini = costruisci_domini(griglia)

    start = time.time()
    successo, revisioni, rimozioni = ac3(domini, vicini)
    tempo = time.time() - start

    celle_risolte = sum(1 for d in domini.values() if len(d) == 1)

    print("Successo AC3:", successo)
    print("Tempo:", round(tempo, 5), "secondi")
    print("Revisioni:", revisioni)
    print("Valori rimossi:", rimozioni)
    print("Celle risolte:", celle_risolte, "/ 81")
