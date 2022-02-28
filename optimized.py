import csv
import itertools
import fonctions

AMOUNT_PER_CUSTOMERS = 500

actions = []
gain_per_action = {}
lst_actions = []
sold = AMOUNT_PER_CUSTOMERS * 100

with open('dataset1_Python+P7.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if float(row['price']) > 0:
            actions.append((row['name'], int(float(row['price']) *100), float(row['profit'])))
#
# for action in actions:
#     benefices.append(fonctions.benefice_for_an_action(action))

# with open('test_matrice.csv', newline='') as csv_file:
#     reader = csv.DictReader(csv_file)
#     for row in reader:
#         actions.append((row['Actions #'], int(row['Cout par action (en euros)']), float(row['Benefice (apres 2 ans)'])))


for action in actions:
    lst_actions.append((action[0], action[1], fonctions.benefice_for_an_action(action)))


# sort_gain = sorted(benefices, key=lambda x: float(x[0][2]), reverse=True)


def dynamic_wallet(argent_disponible, lst_actions):
    matrice = [[0 for _ in range(argent_disponible + 1)] for _ in range(len(lst_actions) + 1)]

    for i in range(1, len(lst_actions) + 1):
        for j in range(1, argent_disponible + 1):
            if lst_actions[i-1][1] <= j:
                matrice[i][j] = max(lst_actions[i-1][2] + matrice[i-1][j-lst_actions[i-1][1]], matrice[i-1][j])
            else:
                matrice[i][j] = matrice[i-1][j]

    w = argent_disponible
    n = len(lst_actions)
    selection = []
    while w >= 0 and n >= 0:
        a = lst_actions[n-1]
        if matrice[n][w] == matrice[n-1][w-a[1]] + a[2]:
            w -= a[1]
            selection.append((a[0], a[1]/100, a[2]/100))
        n -= 1
    return matrice[-1][-1]/100, selection


print(dynamic_wallet(sold, lst_actions))


# print(f"le meilleur rendement est de : {big_win} €. Il faut pour cela investir les actions suivantes : {best_to_do}")
