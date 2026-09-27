""" Программа получает на вход 2 карты игрока, потом 3 карты, потом еще 1 карту и еще одну.
Необходимо вывести комбинации, которые получаются по ходу раздачи (учитывая старшинство).
Потом - по ходу раздачи какие комбинации могут собраться.
"""

import random

from hand_eval import VALUES, combination


cards = []
cards_rus = []
suits = ['♠', '♣', '♥', '♦']
suits_rus = ['пик', 'крестей', 'червей', 'бубен']
values = VALUES
values_rus = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']


for value in values:
    for suit in suits:
        cards.append([value, suit])
cards_copy = cards.copy()

for value in values_rus:
    for suit in suits_rus:
        cards_rus.append([value, suit])

cards_rus_str = []
for i in cards_rus:
    cards_rus_str.append(' '.join(i))


if __name__ == '__main__':
    while True:

        # Ввод 2-х карманных карт
        random_flag = 0
        while True:
            print('2 карманные карты: ', end=' ')
            input_string = input()
            if input_string == '':
                random_flag = 1
                break
            if input_string.count(', ') != 1:
                print('Неверные карты.')
                continue
            my_card1, my_card2 = input_string.split(', ')
            if my_card1 not in cards_rus_str or my_card2 not in cards_rus_str or my_card1 == my_card2:
                print('Неверные карты.')
                continue
            break
        if random_flag == 0:
            my_card1, my_card2 = my_card1.split(), my_card2.split()
            my_card1, my_card2 = cards[cards_rus.index(my_card1)], cards[cards_rus.index(my_card2)]
        else:
            random.shuffle(cards_copy)
            my_card1, my_card2 = cards_copy[0], cards_copy[1]
            del cards_copy[0]
            del cards_copy[0]
        list_of_cards = [my_card1, my_card2]
        print(my_card1, my_card2, combination(list_of_cards))

        # Ввод первых 3-х карт
        random_flag = 0
        while True:
            print('3 первых карты: ', end=' ')
            input_string = input()
            if input_string == '':
                random_flag = 1
                break
            if input_string.count(', ') != 2:
                print('Неверные карты.')
                continue
            card1, card2, card3 = input_string.split(', ')
            if card1 not in cards_rus_str or card2 not in cards_rus_str or card3 not in cards_rus_str \
                    or card1 == card2 or card1 == card3 or card2 == card3:
                print('Неверные карты.')
                continue
            card1, card2, card3 = card1.split(), card2.split(), card3.split()
            card1, card2, card3 = cards[cards_rus.index(card1)], cards[cards_rus.index(card2)], cards[cards_rus.index(card3)]
            if card1 in list_of_cards or card2 in list_of_cards or card3 in list_of_cards:
                print('Неверные карты.')
                continue
            break
        if random_flag == 1:
            random.shuffle(cards_copy)
            card1, card2, card3 = cards_copy[0], cards_copy[1], cards_copy[2]
            del cards_copy[0]
            del cards_copy[0]
            del cards_copy[0]
        list_of_cards.append(card1)
        list_of_cards.append(card2)
        list_of_cards.append(card3)
        print(my_card1, my_card2, '\n', card1, card2, card3, combination(list_of_cards))

        # Ввод 4-й карты
        random_flag = 0
        while True:
            print('4-я карта: ', end=' ')
            card4 = input()
            if card4 == '':
                random_flag = 1
                break
            if card4 not in cards_rus_str:
                print('Неверная карта.')
                continue
            card4 = card4.split()
            card4 = cards[cards_rus.index(card4)]
            if card4 in list_of_cards:
                print('Неверная карта.')
                continue
            break
        if random_flag == 1:
            random.shuffle(cards_copy)
            card4 = cards_copy[0]
            del cards_copy[0]
        list_of_cards.append(card4)
        print(my_card1, my_card2, '\n', card1, card2, card3, card4, combination(list_of_cards))

        # Ввод 5-й карты
        random_flag = 0
        while True:
            print('5-я карта: ', end=' ')
            card5 = input()
            if card5 == '':
                random_flag = 1
                break
            if card5 not in cards_rus_str:
                print('Неверная карта.')
                continue
            card5 = card5.split()
            card5 = cards[cards_rus.index(card5)]
            if card5 in list_of_cards:
                print('Неверная карта.')
                continue
            break
        if random_flag == 1:
            random.shuffle(cards_copy)
            card5 = cards_copy[0]
            del cards_copy[0]
        list_of_cards.append(card5)
        print(my_card1, my_card2, '\n', card1, card2, card3, card4, card5, combination(list_of_cards))
        print('Продолжить? да/нет')
        cont = input()
        if cont == 'нет':
            break
        cards_copy = cards.copy()

'''
4 пик, 5 пик
7 крестей, 4 червей, 9 бубен
валет пик
туз червей

2 пик, 3 крестей
4 пик, 8 пик, 5 крестей
6 червей
7 бубен

король пик, король червей
6 пик, 5 бубен, король бубен
туз крестей
8 бубен
'''
