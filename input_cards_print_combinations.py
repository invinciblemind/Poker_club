""" Программа получает на вход 2 карты игрока, потом 3 карты, потом еще 1 карту и еще одну.
Необходимо вывести комбинации, которые получаются по ходу раздачи (учитывая страшинство).
Потом - по ходу раздачи какие комбинации могут собраться.
"""

import random


def combination(list_of_cards):

    def comb_5(current_suits, current_values_sorted):

        global power_of_combination, values

        # print(current_values_sorted)

        if len(set(current_suits)) == 1:
            if values.index(current_values_sorted[1]) - values.index(current_values_sorted[0]) == 1 and \
                values.index(current_values_sorted[2]) - values.index(current_values_sorted[1]) == 1 and \
                values.index(current_values_sorted[3]) - values.index(current_values_sorted[2]) == 1 and \
                values.index(current_values_sorted[4]) - values.index(current_values_sorted[3]) == 1:
                if current_values_sorted[-1] == 'A':
                    power_of_combination = 10000000
                    return 'Флэш рояль, ' + current_suits[0]
                else:
                    power_of_combination = 9900000 + values.index(current_values_sorted[-1])
                    return 'Стрит флэш, старшая карта ' + current_values_sorted[-1]
            else:
                power_of_combination = 9800000 + values.index(current_values_sorted[-1])
                return 'Флэш, старшая карта ' + current_values_sorted[-1]
        elif len(set(current_values)) == 2:
            if current_values_sorted[0] != current_suits_sorted[1]:
                power_of_combination = 9700000 + values.index(current_values_sorted[1]) * 1000 + values.index(current_values_sorted[0])
                return 'Каре из ' + current_suits_sorted[1] + ', пятая карта ' + current_values_sorted[0]
            elif current_values_sorted[3] != current_suits_sorted[4]:
                power_of_combination = 9700000 + values.index(current_values_sorted[3]) * 1000 + values.index(current_values_sorted[4])
                return 'Каре из ' + current_suits_sorted[3] + ', пятая карта ' + current_values_sorted[4]
            else:
                if current_values_sorted[1] != current_values_sorted[2]:
                    power_of_combination = 9400000 + values.index(current_values_sorted[2]) * 100 + values.index(current_values_sorted[1])
                    return 'Фулл хаус, три ' + current_values_sorted[2] + ', две ' + current_values_sorted[1]
                else:
                    power_of_combination = 9400000 + values.index(current_values_sorted[2]) * 100 + values.index(current_values_sorted[3])
                    return 'Фулл хаус, три ' + current_values_sorted[2] + ', две ' + current_values_sorted[3]
        elif values.index(current_values_sorted[1]) - values.index(current_values_sorted[0]) == 1 and \
                values.index(current_values_sorted[2]) - values.index(current_values_sorted[1]) == 1 and \
                values.index(current_values_sorted[3]) - values.index(current_values_sorted[2]) == 1 and \
                values.index(current_values_sorted[4]) - values.index(current_values_sorted[3]) == 1:
            power_of_combination = 9300000 + values.index(current_values_sorted[4])
            return 'Стрит, старшая карта ' + current_values_sorted[4]
        elif current_values_sorted[4] == current_values_sorted[2]:
            power_of_combination = 9200000 + values.index(current_values_sorted[4]) * 100 + values.index(current_values_sorted[1])
            return 'Сет из ' + current_values_sorted[4] + ', четвертая карта ' + current_values_sorted[1]
        elif current_values_sorted[3] == current_values_sorted[1]:
            power_of_combination = 9200000 + values.index(current_values_sorted[3]) * 100 + values.index(current_values_sorted[4])
            return 'Сет из ' + current_values_sorted[3] + ', четвертая карта ' + current_values_sorted[4]
        elif current_values_sorted[2] == current_values_sorted[0]:
            power_of_combination = 9200000 + values.index(current_values_sorted[2]) * 100 + values.index(current_values_sorted[4])
            return 'Сет из ' + current_values_sorted[2] + ', четвертая карта ' + current_values_sorted[4]
        elif current_values_sorted[3] == current_values_sorted[4] and current_values_sorted[1] == current_values_sorted[2]:
            power_of_combination = 8900000 + values.index(current_values_sorted[3]) * 4000 + values.index(current_values_sorted[1]) * 40 + values.index(current_values_sorted[0])
            return '2 пары из ' + current_values_sorted[3] + ' и ' + current_values_sorted[1] + ', пятая карта ' + current_values_sorted[0]
        elif current_values_sorted[3] == current_values_sorted[4] and current_values_sorted[0] == current_values_sorted[1]:
            power_of_combination = 8900000 + values.index(current_values_sorted[3]) * 4000 + values.index(current_values_sorted[0]) * 40 + values.index(current_values_sorted[2])
            return '2 пары из ' + current_values_sorted[3] + ' и ' + current_values_sorted[0] + ', пятая карта ' + current_values_sorted[2]
        elif current_values_sorted[2] == current_values_sorted[3] and current_values_sorted[0] == current_values_sorted[1]:
            power_of_combination = 8900000 + values.index(current_values_sorted[2]) * 4000 + values.index(current_values_sorted[0]) * 40 + values.index(current_values_sorted[4])
            return '2 пары из ' + current_values_sorted[2] + ' и ' + current_values_sorted[0] + ', пятая карта ' + current_values_sorted[4]
        elif current_values_sorted[3] == current_values_sorted[4]:
            power_of_combination = 8500000 + values.index(current_values_sorted[3]) * 4000 + values.index(current_values_sorted[2]) * 40
            return 'Пара ' + current_values_sorted[3] + ', третья карта ' + current_values_sorted[2]
        elif current_values_sorted[2] == current_values_sorted[3]:
            power_of_combination = 8500000 + values.index(current_values_sorted[2]) * 4000 + values.index(current_values_sorted[4]) * 40
            return 'Пара ' + current_values_sorted[2] + ', третья карта ' + current_values_sorted[4]
        elif current_values_sorted[1] == current_values_sorted[2]:
            power_of_combination = 8500000 + values.index(current_values_sorted[1]) * 4000 + values.index(current_values_sorted[4]) * 40
            return 'Пара ' + current_values_sorted[1] + ', третья карта ' + current_values_sorted[4]
        elif current_values_sorted[0] == current_values_sorted[1]:
            power_of_combination = 8500000 + values.index(current_values_sorted[0]) * 4000 + values.index(current_values_sorted[4]) * 40
            return 'Пара ' + current_values_sorted[0] + ', третья карта ' + current_values_sorted[4]
        else:
            power_of_combination = 8200000 + values.index(current_values_sorted[4]) * 4000
            return 'Старшая карта ' + current_values_sorted[4]
# 19 сил

    global values, suits, power_of_combination, power_of_combination_max
    current_values, current_suits = [], []

    for card in list_of_cards:
        current_values.append(card[0])
        current_suits.append(card[1])

    current_values_sorted = sorted(current_values, key=lambda value: values.index(value))
    cur_values = current_values.copy()
    suits_of_sorted_values = []
    for i in current_values_sorted:
        suits_of_sorted_values.append(current_suits[cur_values.index(i)])
        cur_values[cur_values.index(i)] = '0'

    current_suits_sorted = sorted(current_suits)
    cur_suits = current_suits.copy()
    values_of_sorted_suits = []
    for i in current_suits_sorted:
        values_of_sorted_suits.append(current_values[cur_suits.index(i)])
        cur_suits[cur_suits.index(i)] = '0'

    '''
    print(current_values)
    print(current_suits)
    print('')
    print(current_values_sorted)
    print(suits_of_sorted_values)
    print('')
    print(current_suits_sorted)
    print(values_of_sorted_suits)
    print('')
    '''

    if len(list_of_cards) == 2:
        if current_values_sorted[0] == current_values_sorted[1]:
            return 'Пара ' + current_values_sorted[0]
        return 'Старшая карта ' + current_values_sorted[1]
    elif len(list_of_cards) == 3:
        if current_values_sorted[0] == current_values_sorted[1] and current_values_sorted[0] == current_values_sorted[2]:
            return 'Сет ' + current_values_sorted[0]
        elif current_values_sorted[1] == current_values_sorted[2]:
            return 'Пара ' + current_values_sorted[1]
        elif current_values_sorted[0] == current_values_sorted[1]:
            return 'Пара ' + current_values_sorted[0]
        return 'Старшая карта ' + current_values_sorted[2]
    elif len(list_of_cards) == 4:
        if current_values_sorted[0] == current_values_sorted[1] and \
                current_values_sorted[1] == current_values_sorted[2] and \
                current_values_sorted[2] == current_values_sorted[3]:
            return 'Каре ' + current_values_sorted[0]
        elif current_values_sorted[1] == current_values_sorted[2] and current_values_sorted[2] == current_values_sorted[3]:
            return 'Сет ' + current_values_sorted[1]
        elif current_values_sorted[0] == current_values_sorted[1] and current_values_sorted[1] == current_values_sorted[2]:
            return 'Сет ' + current_values_sorted[0]
        elif current_values_sorted[0] == current_values_sorted[1] and current_values_sorted[2] == current_values_sorted[3]:
            return '2 пары ' + current_values_sorted[2] + ' и ' + current_values_sorted[0]
        elif current_values_sorted[2] == current_values_sorted[3]:
            return 'Пара ' + current_values_sorted[2]
        elif current_values_sorted[1] == current_values_sorted[2]:
            return 'Пара ' + current_values_sorted[1]
        elif current_values_sorted[0] == current_values_sorted[1]:
            return 'Пара ' + current_values_sorted[0]
        return 'Старшая карта ' + current_values_sorted[3]
    elif len(list_of_cards) == 5:
        answer = comb_5(current_suits, current_values_sorted)
        return answer
    elif len(list_of_cards) == 6:
        power_of_combination_max = 0
        power_of_combination = 0
        i_max = 0
        for i in range(6):
            suits_of_sorted_values_copy = suits_of_sorted_values.copy()
            del suits_of_sorted_values_copy[i]
            current_values_sorted_copy = current_values_sorted.copy()
            del current_values_sorted_copy[i]
            comb_5(suits_of_sorted_values_copy, current_values_sorted_copy)
            if power_of_combination > power_of_combination_max:
                power_of_combination_max = power_of_combination
                i_max = i
        suits_of_sorted_values_copy = suits_of_sorted_values.copy()
        del suits_of_sorted_values_copy[i_max]
        current_values_sorted_copy = current_values_sorted.copy()
        del current_values_sorted_copy[i_max]
        answer = comb_5(suits_of_sorted_values_copy, current_values_sorted_copy)
        return answer
    elif len(list_of_cards) == 7:
        power_of_combination_max = 0
        power_of_combination = 0
        i_max = 0
        j_max = 0
        for i in range(6):
            for j in range(i + 1, 7):
                suits_of_sorted_values_copy = suits_of_sorted_values.copy()
                del suits_of_sorted_values_copy[i]
                if i < j:
                    del suits_of_sorted_values_copy[j - 1]
                else:
                    del suits_of_sorted_values_copy[j]
                current_values_sorted_copy = current_values_sorted.copy()
                del current_values_sorted_copy[i]
                if i < j:
                    del current_values_sorted_copy[j - 1]
                else:
                    del current_values_sorted_copy[j]
                comb_5(suits_of_sorted_values_copy, current_values_sorted_copy)
                if power_of_combination > power_of_combination_max:
                    power_of_combination_max = power_of_combination
                    i_max = i
                    j_max = j
        suits_of_sorted_values_copy = suits_of_sorted_values.copy()
        del suits_of_sorted_values_copy[i_max]
        if i_max < j_max:
            del suits_of_sorted_values_copy[j_max - 1]
        else:
            del suits_of_sorted_values_copy[j_max]
        current_values_sorted_copy = current_values_sorted.copy()
        del current_values_sorted_copy[i_max]
        if i_max < j_max:
            del current_values_sorted_copy[j_max - 1]
        else:
            del current_values_sorted_copy[j_max]
        answer = comb_5(suits_of_sorted_values_copy, current_values_sorted_copy)
        return answer




cards = []
cards_rus = []
suits = ['♠', '♣', '♥', '♦']
suits_rus = ['пик', 'крестей', 'червей', 'бубен']
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
values_rus = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'валет', 'дама', 'король', 'туз']

power_of_combination = 0
power_of_combination_max = 0

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
