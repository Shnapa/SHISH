# ****************************************
# Problem 18
# ****************************************
def pattern_number(sequence: (list, str)) -> (list, int):
    """
    (list, str) -> (list, int)
    >>> pattern_number([])
    >>> pattern_number([42])
    >>> pattern_number([1,2])
    >>> pattern_number([1,1])
    ([1], 2)
    >>> pattern_number([1,2,1])
    >>> pattern_number([1,2,3,1,2,3])
    ([1, 2, 3], 2)
    >>> pattern_number([1,2,3,1,2])
    >>> pattern_number([1,2,3,1,2,3,1])
    >>> pattern_number(list(range(10))*20)
    ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 20)
    >>> pattern_number('мама')
    ('ма', 2)
    >>> pattern_number('барабан')
    """
    if len(sequence)<=1:
        return None
    for res in range(1, len(sequence)//2+1):
        pattern = sequence[:res]

        flag = True
        for i in range(res, len(sequence), res):
            if sequence[i:i+res]!= pattern:
                flag = False

        if flag:
            return (pattern, len(sequence)//res)