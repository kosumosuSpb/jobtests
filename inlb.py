"""
Тестовые задания на время (3 часа) для https://inlb.ru
https://coderbyte.com/sl-candidate?promo=inlb-cctw6:python-assessment-0n6dhqf3dd

"""

import unittest


def is_palindrome(string: str) -> bool:
    """Определяет является ли строка палиндромом"""
    string = string.lower()
    new_string = ''
    for letter in string:
        if 'a' <= letter <= 'z':
            new_string += letter

    return new_string == new_string[::-1]


def find_intersection(lst: list) -> str or False:
    """находит пересечения двух строк в списке и смешивает с выданным токеном"""
    CHALLENGE_TOKEN = 'ha17bewxd49'
    str1, str2 = lst
    str1 = str1.split(', ')
    str2 = str2.split(', ')
    intersection = set(str1).intersection(str2)
    intersection = ','.join(sorted(intersection, key=int))

    # itertools был недоступен, так бы использовал zip_longest
    result = ''.join(s1+s2 for s1, s2 in zip(intersection, CHALLENGE_TOKEN))
    end = len(intersection)
    return result + CHALLENGE_TOKEN[end:] if intersection else False


def lru_cache(lst: list) -> str:
    """имитирует работу кэша на 5 элементов"""
    cache = []
    for elem in lst:
        if elem in cache:
            cache.remove(elem)
            cache.append(elem)
        else:
            cache.append(elem)
            if len(cache) > 5:
                cache.pop(0)

    return '-'.join(cache)


class BaseTests(unittest.TestCase):
    """Базовые тесты функций"""

    def test_is_palindrome_1(self):
        test_str = "Noel - sees Leon"
        self.assertTrue(is_palindrome(test_str))

    def test_is_palindrome_2(self):
        test_str = "A war at Tarawa!"
        self.assertTrue(is_palindrome(test_str))

    def test_is_palindrome_3(self):
        test_str = "Anne, I vote more cars race Rome-to-Vienna"
        self.assertTrue(is_palindrome(test_str))

    def test_is_palindrome_not(self):
        test_str = "And I am telling you"
        self.assertFalse(is_palindrome(test_str))

    def test_find_intersection1(self):
        test_list = ["1, 3, 4, 7, 13", "1, 2, 4, 13, 15"]
        self.assertEqual(find_intersection(test_list), "1h,a41,71b3ewxd49")

    def test_find_intersection2(self):
        test_list = ["1, 3, 9, 10, 17, 18", "1, 4, 9, 10"]
        self.assertEqual(find_intersection(test_list), "1h,a91,71b0ewxd49")

    def test_find_intersection_not(self):
        test_list = ["1, 3, 9, 10, 17, 18", "5, 6, 11, 12"]
        self.assertEqual(find_intersection(test_list), False)

    def test_lru_cache1(self):
        test_list = ["A", "B", "A", "C", "A", "B"]
        self.assertEqual(lru_cache(test_list), 'C-A-B')

    def test_lru_cache2(self):
        test_list = ["A", "B", "C", "D", "E", "D", "Q", "Z", "C"]
        self.assertEqual(lru_cache(test_list), 'E-D-Q-Z-C')


if __name__ == '__main__':
    unittest.main()
