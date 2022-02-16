# coding: cp1251


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


if __name__ == '__main__':
    print(expressions_finder())