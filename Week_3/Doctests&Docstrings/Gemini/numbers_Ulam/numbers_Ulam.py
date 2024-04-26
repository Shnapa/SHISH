# ****************************************
# Problem 20
# ****************************************
def numbers_Ulam(n):
    """
    >>> numbers_Ulam(10)
    [1, 2, 3, 4, 6, 8, 11, 13, 16, 18]
    >>> numbers_Ulam(2)
    [1, 2]
    >>> numbers_Ulam(1)
    [1]
    """
    if n < 1:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 2]
    else:
        ulam_set = [1, 2]
        num = 3
        while len(ulam_set) < n:
            count = 0
            for i in range(len(ulam_set)):
                for j in range(i+1, len(ulam_set)):
                    if ulam_set[i] + ulam_set[j] == num:
                        count += 1
                        if count > 1:
                            break
                if count > 1:
                    break
            if count == 1:
                ulam_set.append(num)
            num += 1
        return ulam_set