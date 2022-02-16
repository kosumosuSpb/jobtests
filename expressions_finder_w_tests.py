import unittest


def expressions_finder(start=9, stop=0, goal=200):
    """
    ������� �������� '+', '-', ��� '' (������)
    ����� ������� �� 9 �� 0 (� ����� �������, ����� ����� ������)
    ���, ����� � ���������� ���������� 200 (����� ����� ������).
    ��������: 98+76-5+43-2-10=200.
    :param start: ������ ������������������ (��-��������� = 9)
    :param stop: ����� ������������������ (��-��������� = 0)
    :param goal: ��������� ��������� (��-��������� = 200)
    :return: ������ ���������
    """

    def expr_generator(n):
        """
        ��������������� ����������� �������-���������,
        ������� ���������� ��� ��������� �������� ����������
        '+', '-' � '' ����� �������
        :param n: ������ ������������������
        :return: ������� ����������
        """

        if n == stop:
            yield str(n)

        else:
            s1 = str(n)
            for s2 in expr_generator(n - 1):
                yield s1 + s2
                yield s1 + '+' + s2
                yield s1 + '-' + s2

    return [expr for expr in expr_generator(start) if eval(expr) == goal]


class TestTwoHundred(unittest.TestCase):
    def test_200_example(self):
        example = '98+76-5+43-2-10'
        self.assertIn(example, expressions_finder())

    def test_200_complete(self):
        assertion_list = ['9-8-7-6-5+4+3+210', '9-8+7-6-5-4-3+210', '98+76-5+43-2-10',
                          '98-7+65+43+2-1+0', '98-7+65+43+2-1-0']
        self.assertEqual(expressions_finder(), assertion_list)

    def test_3_0_4(self):
        assertion_list = ['3+2-1+0', '3+2-1-0']
        self.assertEqual(expressions_finder(3, 0, 4), assertion_list)

    def test_3_1_4(self):
        assertion_list = ['3+2-1']
        self.assertEqual(expressions_finder(3, 1, 4), assertion_list)


if __name__ == '__main__':
    unittest.main()