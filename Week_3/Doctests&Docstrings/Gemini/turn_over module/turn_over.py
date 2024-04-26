# ****************************************
# Problem 23
# ****************************************
def turn_over(n: int, lst: list) -> list:
    """
    Reverse first n items of the list and return it. If n <= 0, return
    the empty list. Do not consume MORE than n items of iterable.

    >>> turn_over(4, ['f', 'o', 'o', 't', 'b', 'a', 'l', 'l'])
    ['t', 'o', 'o', 'f', 'b', 'a', 'l', 'l']
    >>> turn_over(5, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [5, 4, 3, 2, 1, 6, 7, 8, 9, 10]
    >>> turn_over(10, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    >>> turn_over(-5, [])
    []
    """
    if n == 0:
        return lst  # Handle n is zero

    # Limit n to the length of the list to avoid out-of-bounds access
    n = min(n, len(lst))

    # Reverse the first n elements using slicing
    return lst[:n][::-1] + lst[n:]
