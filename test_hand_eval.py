""" Тесты оценки рук. Запуск: python3 -m unittest -v """

import unittest

from hand_eval import (best_hand, combination, evaluate_5,
                       HIGH_CARD, PAIR, TWO_PAIRS, SET, STRAIGHT, FLUSH,
                       FULL_HOUSE, QUADS, STRAIGHT_FLUSH, ROYAL_FLUSH)

SUITS = {'s': '♠', 'c': '♣', 'h': '♥', 'd': '♦'}


def hand(text):
    """ 'Ks Kh 10d' -> [['K', '♠'], ['K', '♥'], ['10', '♦']] """
    return [[card[:-1], SUITS[card[-1]]] for card in text.split()]


def category(text):
    return best_hand(hand(text))[0][0]


def score(text):
    return best_hand(hand(text))[0]


class TestCategories(unittest.TestCase):
    """ Каждая комбинация распознаётся на 5 картах. """

    def test_all_categories(self):
        cases = [
            ('As Ks Qs Js 10s', ROYAL_FLUSH),
            ('9h 8h 7h 6h 5h', STRAIGHT_FLUSH),
            ('Ad 2d 3d 4d 5d', STRAIGHT_FLUSH),
            ('Ks Kh Kd Kc 5c', QUADS),
            ('Ks Kh Kd 5s 5c', FULL_HOUSE),
            ('As Js 9s 5s 3s', FLUSH),
            ('10s 9h 8d 7c 6c', STRAIGHT),
            ('As Kh Qd Jc 10c', STRAIGHT),
            ('As 2h 3d 4c 5c', STRAIGHT),
            ('7s 7h 7d Kc 2c', SET),
            ('9s 9h 4d 4c Ac', TWO_PAIRS),
            ('Js Jh 8d 4c 2c', PAIR),
            ('As Jh 8d 4c 2c', HIGH_CARD),
        ]
        for cards, expected in cases:
            with self.subTest(cards=cards):
                self.assertEqual(category(cards), expected)

    def test_almost_straight_is_not_straight(self):
        self.assertEqual(category('Ks Ah 2d 3c 4c'), HIGH_CARD)  # стрит не "заворачивает" через туза
        self.assertEqual(category('10s 9h 8d 7c 5c'), HIGH_CARD)


class TestFewerCards(unittest.TestCase):
    """ Префлоп и неполные руки: стрит и флэш из 2-4 карт не собираются. """

    def test_preflop(self):
        self.assertEqual(category('As Ah'), PAIR)
        self.assertEqual(category('As Ks'), HIGH_CARD)

    def test_four_cards(self):
        self.assertEqual(category('Ks Kh Kd Kc'), QUADS)
        self.assertEqual(category('Ks Kh 5d 5c'), TWO_PAIRS)
        self.assertEqual(category('Ks Qs Js 10s'), HIGH_CARD)


class TestSevenCards(unittest.TestCase):
    """ Из 6-7 карт выбирается сильнейшая пятёрка. """

    def test_full_house_from_seven(self):
        self.assertEqual(score('Ks Kh Kd 5s 5c 2h 9d'), (FULL_HOUSE, [13, 5]))

    def test_quads_from_seven(self):
        self.assertEqual(score('Ks Kh Kd Kc 5c 2h 9d'), (QUADS, [13, 9]))

    def test_two_sets_make_full_house(self):
        self.assertEqual(score('8s 8h 8d 3s 3c 3h Ad'), (FULL_HOUSE, [8, 3]))

    def test_three_pairs_best_two_plus_kicker(self):
        # Пары A, 9, 4 и кикер 2: берём A и 9, кикером идёт четвёрка из третьей пары.
        self.assertEqual(score('As Ah 9d 9c 4s 4h 2d'), (TWO_PAIRS, [14, 9, 4]))

    def test_flush_beats_straight(self):
        self.assertEqual(category('9s 8h 7s 6s 5d 2s Ks'), FLUSH)

    def test_full_house_beats_flush(self):
        self.assertEqual(category('Ks Kh Kd 5s 5c 2s 9s'), FULL_HOUSE)

    def test_straight_flush_beats_set(self):
        self.assertEqual(score('9h 8h 7h 6h 5h 9s 9d'), (STRAIGHT_FLUSH, [9]))

    def test_best_straight_chosen(self):
        self.assertEqual(score('As 2h 3d 4c 5c 6h 7d'), (STRAIGHT, [7]))

    def test_wheel_from_seven(self):
        self.assertEqual(score('As 2h 3d 4c 5c Kh Kd'), (STRAIGHT, [5]))

    def test_six_cards(self):
        self.assertEqual(score('Ks Kh 5d 5c 5s 2h'), (FULL_HOUSE, [5, 13]))


class TestComparison(unittest.TestCase):
    """ Оценки двух рук правильно сравниваются между собой (кикеры). """

    def assertStronger(self, stronger, weaker):
        self.assertGreater(score(stronger), score(weaker))

    def test_kickers(self):
        self.assertStronger('As Ah Kd 7c 2c', 'Ad Ac Qd 7c 2c')        # пара, кикер K > Q
        self.assertStronger('As Ah Kd 7c 3c', 'Ad Ac Kh 7d 2c')        # пара, последний кикер
        self.assertStronger('9s 9h 4d 4c Ac', '9d 9c 4s 4h Kc')        # 2 пары, кикер
        self.assertStronger('As Js 9s 5s 3s', 'Ah Jh 9h 5h 2h')        # флэш, пятая карта
        self.assertStronger('As Kh Qd Jc 9c', 'As Kh Qd Jc 8c')        # старшая карта

    def test_category_order(self):
        order = ['As Jh 8d 4c 2c', 'Js Jh 8d 4c 2c', '9s 9h 4d 4c Ac',
                 '7s 7h 7d Kc 2c', '10s 9h 8d 7c 6c', 'As Js 9s 5s 3s',
                 'Ks Kh Kd 5s 5c', 'Ks Kh Kd Kc 5c', '9h 8h 7h 6h 5h',
                 'As Ks Qs Js 10s']
        scores = [score(cards) for cards in order]
        self.assertEqual(scores, sorted(scores))

    def test_wheel_is_lowest_straight(self):
        self.assertStronger('2s 3h 4d 5c 6c', 'As 2h 3d 4c 5c')

    def test_equal_hands_different_suits(self):
        self.assertEqual(score('As Kh Qd Jc 9c'), score('Ah Kd Qc Js 9s'))


class TestDescribe(unittest.TestCase):
    """ Текстовые описания, включая руки, на которых старая версия ошибалась. """

    def test_texts(self):
        cases = [
            ('Ks Kh Kd 5s 5c', 'Фулл хаус, три K, две 5'),
            ('Ks Kh Kd Kc 5c', 'Каре из K, кикер 5'),
            ('Ks Kh Kd 5s 5c 2h 9d', 'Фулл хаус, три K, две 5'),
            ('As 2h 3d 4c 5c', 'Стрит, старшая карта 5'),
            ('As Ks Qs Js 10s', 'Флэш рояль'),
            ('9s 9h 4d 4c Ac', '2 пары из 9 и 4, кикер A'),
            ('Js Jh 8d 4c 2c', 'Пара J, кикеры 8 4 2'),
            ('As Ah', 'Пара A'),
            ('As Js 9s 5s 3s', 'Флэш: A J 9 5 3'),
        ]
        for cards, expected in cases:
            with self.subTest(cards=cards):
                self.assertEqual(combination(hand(cards)), expected)


class TestEvaluate5(unittest.TestCase):

    def test_order_of_cards_does_not_matter(self):
        self.assertEqual(evaluate_5(hand('5c 5s Kd Kh Ks')), evaluate_5(hand('Ks Kh Kd 5s 5c')))


if __name__ == '__main__':
    unittest.main()
