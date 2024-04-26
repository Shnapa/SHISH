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
    if not isinstance(s1, str) or not isinstance(s2, str):
        return None
    all_letters = set(s1) | set(s2)  # Combine letters from both strings using sets
    return ''.join(sorted(all_letters))