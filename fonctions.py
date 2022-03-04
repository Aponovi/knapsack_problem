import math

AMOUNT_PER_CUSTOMERS = 500


def benefice_for_an_action(action, cents=True):
    gain = (float(action[1]) * float(action[2])) / 100
    if cents:
        gain = math.floor(gain)
    else:
        gain = math.floor(round(gain * 100, 2)) / 100
    return gain


def verification(chosen_actions):
    sold = 0
    for chosen_action in chosen_actions:
        sold += round(float(chosen_action[1]), 2)
    if sold > AMOUNT_PER_CUSTOMERS:
        return False
    else:
        return True


def total_gain(chosen_actions, cents=True):
    gain = 0
    for chosen_action in chosen_actions:
        retour = benefice_for_an_action(chosen_action, cents)
        gain += retour
    return gain


def dynamic_wallet(argent_disponible, lst_actions):
    matrice = [[0 for _ in range(argent_disponible + 1)] for _ in range(len(lst_actions) + 1)]

    for i in range(1, len(lst_actions) + 1):
        for j in range(1, argent_disponible + 1):
            if lst_actions[i - 1][1] <= j:
                matrice[i][j] = max(lst_actions[i - 1][2] + matrice[i - 1][j - lst_actions[i - 1][1]],
                                    matrice[i - 1][j])
            else:
                matrice[i][j] = matrice[i - 1][j]

    w = argent_disponible
    n = len(lst_actions)
    selection = []
    while w >= 0 and n >= 0:
        a = lst_actions[n - 1]
        if matrice[n][w] == matrice[n - 1][w - a[1]] + a[2]:
            w -= a[1]
            selection.append((a[0], a[1] / 100, a[2] / 100))
        n -= 1
    return matrice[-1][-1] / 100, selection
