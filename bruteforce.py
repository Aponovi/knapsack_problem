import csv
import itertools
import fonctions

AMOUNT_PER_CUSTOMERS = 500

actions = []
sold = AMOUNT_PER_CUSTOMERS


with open('rendement_actions.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        actions.append((row['name'], int(float(row['price'])), float(row['profit'])))

print(f"\nSomme à investir : {sold} €\n")

combinaisons = []
results = []
big_win = 0
best_to_do = []

for i in range(1, len(actions)+1):
    els = [list(x) for x in itertools.combinations(actions, i)]
    combinaisons.extend(els)

for combinaison in combinaisons:
    if fonctions.verification(combinaison):
        win = round(fonctions.total_gain(combinaison, False), 2)
        results.append((combinaison, win))
        if win > big_win:
            big_win = win
            best_to_do = combinaison

print(f"le meilleur rendement est de : {big_win} €. Il faut pour cela investir les actions suivantes : {best_to_do}")
