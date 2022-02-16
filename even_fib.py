import unittest


def even_fib(n: int) -> list:
    """
    Выводит n чётных элементов последовательности 
    чисел Фибоначчи

    :param n: количество элементов 
    :return: список элементов
    """""
    result = []
    a, b = 0, 1
    while len(result) < n:
        if a % 2 == 0:
            result.append(a)
        a, b = b, a + b

    return result


class TestOddFibonacci(unittest.TestCase):
    def test_fib_4(self):
        result = [0, 2, 8, 34]
        self.assertEqual(even_fib(4), result)


if __name__ == '__main__':
    unittest.main()