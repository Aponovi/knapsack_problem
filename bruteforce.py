import csv
import itertools
import fonctions

AMOUNT_PER_CUSTOMERS = 500

actions = []
gain_per_action = {}
benefices = []


with open('rendement_actions.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        actions.append((row['Actions #'], row['Cout par action (en euros)'], row['Benefice (apres 2 ans)']))

# print("liste des actions : " + str(actions))


for action in actions:
    benefices.append(fonctions.benefice_for_an_action(action))

# sort_gain = sorted(benefices, key=lambda x: x[1], reverse=True)
#
# for i in sort_gain:
#     print(i[0], i[1])

sold = AMOUNT_PER_CUSTOMERS
# benefices = 0
# chosen1 = []

# print(f"\nSomme à investir : {sold} €\n")

# for action in sort_gain:
#     invest = float(action[0][1])
#     if sold > float(action[0][1]):
#         sold = sold - invest
#         benefices += action[1]
#         benefices = round(benefices, 2)
#         chosen1.append(action)
#         print(f"action achetée : {action[0][0]} {invest} bénéfices (après 2 ans) : {action[1]}")
#         print(f"cumul benefices : {benefices}")
#         print(f"\nsolde : {sold} €")
# print(f"\nsolde : {sold} €")
# print(f"bénéfice au bout de deux ans : {benefices} €")

results = []

lst = actions
combinaisons = []
big_win = 0
best_to_do = []

for i in range(1, len(lst)+1):
    els = [list(x) for x in itertools.combinations(lst, i)]
    combinaisons.extend(els)

for combinaison in combinaisons:
    if fonctions.verification(combinaison):
        win = round(fonctions.total_gain(combinaison), 2)
        results.append((combinaison, win))
        if win > big_win:
            big_win = win
            best_to_do = combinaison

# print(results)
print(f"le meilleur rendement est de : {big_win} €. Il faut pour cela investir les actions suivantes : {best_to_do}")
