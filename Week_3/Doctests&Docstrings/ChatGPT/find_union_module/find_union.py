# ****************************************
# Problem 14
# ****************************************
def find_union(s1: str, s2: str) -> str:
    """
    (str, str) -> str
    Find and return string of all letters in alphabetic order that
    are present in either strings. If arguments aren't strings function should
    return None.

    >>> find_union("aaabb", "bbbbccc")
    'abc'
    >>> find_union("aZAbc", "zzYYxp")
    'AYZabcpxz'
    >>> find_union("sfdfsdf", 2015)
    """
    if not (isinstance(s1, str) and isinstance(s2, str)):
        return None

    # Create sets of unique characters from each string
    set1 = set(s1)
    set2 = set(s2)

    # Merge the sets and sort the result
    union_set = sorted(set1.union(set2))

    # Join the sorted characters into a string
    union_str = ''.join(union_set)

    return union_str
