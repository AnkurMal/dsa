import math


def min_squares(n):
    """see Lagrange's four-square theorem.md"""

    def is_square(n):
        root = int(math.sqrt(n))
        return root * root == n

    if is_square(n):
        return 1

    for i in range(1, int(math.sqrt(n)) + 1):
        if is_square(n - i * i):
            return 2

    while n > 0 and n % 4 == 0:
        n //= 4
    if n % 8 == 7:
        return 4

    return 3
