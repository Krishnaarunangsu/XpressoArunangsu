# Python fixed set of arguments


class Addition:
    def __init__(self, a, b):
        """

        :param a: int
        :param b: int
        """
        self.a = a
        print(a)
        self.b = b

    def my_sum(self):
        """

        :return: int
        """
        return self.a + self.b


if __name__ == "__main__":
    print('A')
    addition = Addition(3, 5)
    sum_two_num = addition.my_sum()
    print(f'Sum of Two Numbers:{sum_two_num}')
