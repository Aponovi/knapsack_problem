import math

AMOUNT_PER_CUSTOMERS = 500


def benefice_for_an_action(action):
    gain = (float(action[1]) * float(action[2]))/100
    gain = math.floor(gain)
    return gain


def verification(chosen_actions):
    sold = 0
    for chosen_action in chosen_actions:
        sold += round(float(chosen_action[1]), 2)
    if sold > AMOUNT_PER_CUSTOMERS:
        return False
    else:
        return True


def total_gain(chosen_actions):
    gain = 0
    for chosen_action in chosen_actions:
        retour = benefice_for_an_action(chosen_action)
        gain += float(retour[1])
    return gain
