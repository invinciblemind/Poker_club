""" Оценка покерной руки (техасский холдем).

Карта - пара [значение, масть], например ['K', '♠'].
Оценка руки - кортеж (категория, [ранги для сравнения]); кортежи сравниваются
обычным > / <, поэтому сильнейшая рука - это просто max().
"""

from collections import Counter
from itertools import combinations

VALUES = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
RANK = {value: rank for rank, value in enumerate(VALUES, start=2)}  # '2' -> 2, ..., 'A' -> 14
VALUE_OF_RANK = {rank: value for value, rank in RANK.items()}

(HIGH_CARD, PAIR, TWO_PAIRS, SET, STRAIGHT, FLUSH,
 FULL_HOUSE, QUADS, STRAIGHT_FLUSH, ROYAL_FLUSH) = range(10)


def evaluate_5(cards):
    """ Оценка руки из 5 карт или меньше (на префлопе/флопе стрит и флэш невозможны). """
    ranks = [RANK[value] for value, suit in cards]
    counts = Counter(ranks)
    # Ранги по убыванию: сначала по количеству повторов, потом по старшинству.
    # Для K K K 5 5 получится [K, 5], для 9 9 4 4 A - [9, 4, A].
    grouped = sorted(counts, key=lambda rank: (counts[rank], rank), reverse=True)
    pattern = sorted(counts.values(), reverse=True)

    is_flush = len(cards) == 5 and len({suit for value, suit in cards}) == 1
    straight_top = None
    if len(cards) == 5 and len(counts) == 5:
        if max(ranks) - min(ranks) == 4:
            straight_top = max(ranks)
        elif set(ranks) == {14, 2, 3, 4, 5}:  # "колесо" A-2-3-4-5, туз считается единицей
            straight_top = 5

    if is_flush and straight_top:
        return (ROYAL_FLUSH if straight_top == 14 else STRAIGHT_FLUSH), [straight_top]
    if pattern[0] == 4:
        return QUADS, grouped
    if pattern[:2] == [3, 2]:
        return FULL_HOUSE, grouped
    if is_flush:
        return FLUSH, grouped
    if straight_top:
        return STRAIGHT, [straight_top]
    if pattern[0] == 3:
        return SET, grouped
    if pattern[:2] == [2, 2]:
        return TWO_PAIRS, grouped
    if pattern[0] == 2:
        return PAIR, grouped
    return HIGH_CARD, grouped


def best_hand(cards):
    """ Лучшая пятёрка из 2-7 карт: возвращает (оценка, карты этой пятёрки). """
    if len(cards) <= 5:
        return evaluate_5(cards), list(cards)
    five = max(combinations(cards, 5), key=evaluate_5)
    return evaluate_5(five), list(five)


def describe(score):
    """ Текстовое описание оценки руки. """
    category, ranks = score
    names = [VALUE_OF_RANK[rank] for rank in ranks]

    def kickers(rest):
        if not rest:
            return ''
        return (', кикер ' if len(rest) == 1 else ', кикеры ') + ' '.join(rest)

    if category == ROYAL_FLUSH:
        return 'Флэш рояль'
    if category == STRAIGHT_FLUSH:
        return 'Стрит флэш, старшая карта ' + names[0]
    if category == QUADS:
        return 'Каре из ' + names[0] + kickers(names[1:])
    if category == FULL_HOUSE:
        return 'Фулл хаус, три ' + names[0] + ', две ' + names[1]
    if category == FLUSH:
        return 'Флэш: ' + ' '.join(names)
    if category == STRAIGHT:
        return 'Стрит, старшая карта ' + names[0]
    if category == SET:
        return 'Сет из ' + names[0] + kickers(names[1:])
    if category == TWO_PAIRS:
        return '2 пары из ' + names[0] + ' и ' + names[1] + kickers(names[2:])
    if category == PAIR:
        return 'Пара ' + names[0] + kickers(names[1:])
    return 'Старшая карта ' + names[0] + kickers(names[1:])


def combination(cards):
    """ Описание лучшей комбинации из переданных карт. """
    score, five = best_hand(cards)
    return describe(score)
