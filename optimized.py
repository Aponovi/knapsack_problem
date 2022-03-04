import csv
import fonctions

AMOUNT_PER_CUSTOMERS = 500

actions = []
list_actions = []
sold = AMOUNT_PER_CUSTOMERS * 100

with open('dataset1_Python+P7.csv', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        if float(row['price']) > 0:
            actions.append((row['name'], int(float(row['price']) * 100), float(row['profit'])))

for action in actions:
    list_actions.append((action[0], action[1], fonctions.benefice_for_an_action(action)))


big_win, best_to_do = fonctions.dynamic_wallet(sold, list_actions)

print(f"le meilleur rendement est de : {big_win} €.\n Il faut pour cela investir les actions suivantes : {best_to_do}")
