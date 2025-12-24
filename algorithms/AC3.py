# implementazione dell'algoritmo AC3

def revise(domini, Xi, Xj):
    """
    Rende l'arco (Xi, Xj) consistente.
    Rimuove da dominio(Xi) i valori che non hanno supporto in Xj.
    """
    rimosso = False

    for x in set(domini[Xi]):  # copia per evitare problemi
        # esiste almeno un y in Xj tale che x != y?
        if not any(x != y for y in domini[Xj]):
            domini[Xi].remove(x)
            rimosso = True

    return rimosso


def ac3(domini, vicini):
    """
    Algoritmo AC3.
    Restituisce:
    - successo (True/False)
    - numero di revisioni
    - numero di valori rimossi
    """
    from collections import deque

    coda = deque()
    for Xi in domini:
        for Xj in vicini[Xi]:
            coda.append((Xi, Xj))

    revisioni = 0
    rimozioni = 0

    while coda:
        Xi, Xj = coda.popleft()
        revisioni += 1

        dimensione_precedente = len(domini[Xi])

        if revise(domini, Xi, Xj):
            rimozioni += dimensione_precedente - len(domini[Xi])

            if len(domini[Xi]) == 0:
                return False, revisioni, rimozioni

            for Xk in vicini[Xi]:
                if Xk != Xj:
                    coda.append((Xk, Xi))

    return True, revisioni, rimozioni
