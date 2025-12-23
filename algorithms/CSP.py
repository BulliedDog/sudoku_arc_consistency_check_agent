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
    Per ogni cella (r,c) calcola l'insieme delle celle vicine
    ovvero il blocco 3x3
    """
    # come chiave del dizionario posso usare le tuple (r,c) perché in python sono immutabili
    vicini = {(r, c): set() for r in range(9) for c in range(9)}

    for r in range(9):
        for c in range(9):

            # stessa riga e stessa colonna
            for k in range(9):
                if k != c:
                    vicini[(r, c)].add((r, k))
                if k != r:
                    vicini[(r, c)].add((k, c))

            # stesso blocco 3x3
            blocco_r = (r // 3) * 3
            blocco_c = (c // 3) * 3

            for i in range(blocco_r, blocco_r + 3):
                for j in range(blocco_c, blocco_c + 3):
                    if (i, j) != (r, c):
                        vicini[(r, c)].add((i, j))

    return vicini
