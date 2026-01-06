from collections import deque

# Implementazione AC4

def ac4(domini, vicini):
    """
    Implementazione dell'algoritmo AC4 per il Sudoku
    Restituisce:
    - successo/fallimento (True/False)
    - numero di revisioni (aggiornamenti di contatori)
    - numero di valori rimossi
    - numero di contatori
    - numero di supporti
    """
    contatore_supporti = {}
    supportati_da = {}
    coda = deque()

    revisioni = 0
    rimozioni = 0

    # Inizializzazione
    for Xi in domini:
        for x in domini[Xi]:
            supportati_da[(Xi, x)] = []

    for Xi in domini:
        for Xj in vicini[Xi]:
            for x in domini[Xi]:
                count = 0
                for y in domini[Xj]:
                    if x != y:  # vincolo di disuguaglianza del Sudoku, criterio di supporto
                        count += 1
                        supportati_da[(Xj, y)].append((Xi, x))
                contatore_supporti[(Xi, x, Xj)] = count

                if count == 0:
                    coda.append((Xi, x))

    max_coda = len(coda)
    
    # Propagazione delle inferenze
    while coda:
        max_coda = max(max_coda, len(coda)) # picco massimo dimensione coda
        Xi, x = coda.popleft()

        if x not in domini[Xi]:
            continue

        domini[Xi].remove(x)
        rimozioni += 1

        # Per ogni valore che dipendeva da (Xi = x)
        for (Xk, v) in supportati_da[(Xi, x)]:
            key = (Xk, v, Xi)
            contatore_supporti[key] -= 1
            revisioni += 1

            # Se il valore v perde tutti i supporti si aggiunge alla coda di eliminazione
            if contatore_supporti[key] == 0:
                coda.append((Xk, v))

        if len(domini[Xi]) == 0:
            return False, revisioni, rimozioni, len(contatore_supporti), len(supportati_da), max_coda

    return True, revisioni, rimozioni, len(contatore_supporti), len(supportati_da), max_coda
