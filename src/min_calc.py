# Minimum Calculation


z=0
def min_calculation(data):
    """
    Calculation of the median
    :param data:
    :return:
    """
    global z
    z= min(data)
    print(z)
    return z


if __name__ == "__main__":
    data1=[1, 2, 3, 4, 5]
    min_of_the_series = min_calculation(data1)
    print("Min: ", min_of_the_series)
