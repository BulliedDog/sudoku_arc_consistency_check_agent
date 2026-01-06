# Costruzione del CSP: domini e vicini

def costruisci_domini(griglia):
    """
    Crea il dizionario dei domini.
    Chiave -> (riga, colonna)
    Valore -> dominio
    """
    domini = {}
    for r in range(9):
        for c in range(9):
            if griglia[r][c] == '0':
                domini[(r, c)] = set(range(1, 10))
            else:
                domini[(r, c)] = {int(griglia[r][c])}
    return domini


def costruisci_vicini():
    """
    Per ogni cella (r,c) calcola l'insieme delle celle "vicine"
    ovvero il blocco 3x3 e le celle sulla stessa riga e colonna.
    """
    # Come chiave del dizionario posso usare le tuple (r,c) perché in python sono immutabili
    # 81 pairs associati a quelli della griglia, ognuno con le key delle celle vincolate
    vicini = {(r, c): set() for r in range(9) for c in range(9)}

    for r in range(9):
        for c in range(9):
            # Per ogni riga e per ogni colonna aggiungo tutte le celle della stessa riga & colonna in vicini[(r,c)]
            for k in range(9):
                if k != c:
                    vicini[(r, c)].add((r, k)) # Aggiunge tutti quelli sulla stessa riga
                if k != r:
                    vicini[(r, c)].add((k, c)) # Aggiunge tutti quelli sulla stessa colonna

            # Stesso blocco 3x3
            blocco_r = (r // 3) * 3 # Riga del blocco con divisione floor
            blocco_c = (c // 3) * 3 # Colonna del blocco con divisione floor
            for i in range(blocco_r, blocco_r + 3):
                for j in range(blocco_c, blocco_c + 3):
                    if (i, j) != (r, c):
                        vicini[(r, c)].add((i, j))
    return vicini

def stampa_sudoku_da_domini(domini):
    for r in range(9):
        riga = ""
        for c in range(9):
            valore = next(iter(domini[(r, c)]))
            riga += f"{valore} "
        print(riga)