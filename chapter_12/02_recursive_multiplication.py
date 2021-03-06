# recursive multiplication

# 2. Рекурсивное умножение.
# Разработайте рекурсивную функцию, которая принимает два аргумента в
# параметры х и у. Данная функция должна вернуть значение произведения х на
# у. При этом умножение должно быть выполнено, как повторяющееся сложение,
# следующим образом: 7 х 4 = 4 + 4 + 4 + 4 + 4 + 4 + 4.
# (Для того чтобы упростить функцию, исходите из того, что х и у будут
# всегда содержать положительные ненулевые целые числа.)
#
def main():
    x = int(input("Enter a positive integer for X: "))
    y = int(input("Enter a positive integer for Y: "))
    print(mul_x_y(x, y))


def mul_x_y(x, y):
    if x <= 0:
        return 0
    return y + mul_x_y(x - 1, y)


main()
