from collections import deque

# Implementazione dell'algoritmo AC3
# NB: AC3 non controlla il vincolo globale Tuttediverse(riga/colonna) oppure Tuttediverse(blocco)
# ma controlla solo i vincoli binari con le celle in vicini corrispondenti propagando l'inferenza,
# quindi non è detto che risolva il sudoku! Per quello bisogna ricorrere a un algoritmo di ricerca locale o con backtracking

def revise(domini, Xi, Xj):
    """
    Applica l'inferenza a tutti gli effetti
    Rende l'arco (Xi, Xj) consistente elimininando gli elementi dal dominio di Xi che non hanno consistenza d'arco in Xj vicino.
    Rimuove da dominio(Xi) i valori che non hanno consistenza d'arco in Xj.
    """
    rimosso = False

    for x in set(domini[Xi]):
        # Dato x valore preso dal dominio di Xi e dato y valore preso dal dominio di Xj ovvero nodo vicino:
        # esiste almeno un elemento y != x? Se sì la consistenza d'arco è preservata perchè 
        # ogni elemento dei vicini dovrà essere scelto diverso da quello x qualora venisse assunto in Xi con la ricerca
        if not any(x != y for y in domini[Xj]):
            domini[Xi].remove(x) # Rimuovo il valore che non preserva la consistenza
            rimosso = True # Notifico di aver rimosso un elemento, così da revisionare gli archi degli altri nodi vicini

    return rimosso


def ac3(domini, vicini):
    """
    Restituisce:
    - successo (True/False)
    - numero di revisioni
    - numero di valori rimossi
    """
    # All'inizio ci metto tutti gli archi di consistenza, ovvero pair di ((r,c) = cella corrente,(r,c) = cella vicina)
    coda = deque() # coda
    for Xi in domini:
        for Xj in vicini[Xi]:
            coda.append((Xi, Xj))

    revisioni = 0
    rimozioni = 0
    max_coda = len(coda)
    
    while any(coda):
        max_coda = max(max_coda, len(coda))
        Xi, Xj = coda.popleft()
        revisioni += 1

        dimensione_precedente = len(domini[Xi])

        if revise(domini, Xi, Xj): # Se ritorna true, notifica di aver rimosso qualche elemento da dominio Xi
            rimozioni += dimensione_precedente - len(domini[Xi])

            if len(domini[Xi]) == 0:
                return False, revisioni, rimozioni, max_coda # Unico caso di fallimento, un dominio è vuoto => insoddisfacibile!

            for Xk in vicini[Xi]:
                if Xk != Xj: # Altrimenti rieffettua il revise() su quello appena revisionato (Xi, Xj)!
                    coda.append((Xk, Xi)) # Propagazione di revisione, solo quando il dominio di Xi è stato ridotto

    return True, revisioni, rimozioni, max_coda
