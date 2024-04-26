# ****************************************
# Problem 19
# ****************************************
def one_swap_sorting(sequence: list) -> bool:
    """
    >>> one_swap_sorting([0,1,2,3])
    False
    >>> one_swap_sorting([])
    False
    >>> one_swap_sorting([42])
    False
    >>> one_swap_sorting([3,2])
    True
    >>> one_swap_sorting([2,2])
    False
    >>> one_swap_sorting([5,2,3,4,1,6])
    True
    >>> one_swap_sorting([1,2,3,5,4])
    True
    """
    n = len(sequence)
    if n <= 1:
        return False  # Empty or single-element sequence cannot be sorted

    # Find the first element out of order (increasing order)
    i = 0
    while i < n - 1 and sequence[i] <= sequence[i + 1]:
        i += 1

    # If the sequence is already sorted, return False
    if i == n - 1:
        return False

    # Find the first element greater than the misplaced element (from the right)
    j = n - 1
    while j > i and sequence[j] <= sequence[i]:
        j -= 1

    # If no element is greater than the misplaced element, return False
    if j == i:
        return True

    # Swap the misplaced element with the element at j (potential correction)
    sequence[i], sequence[j] = sequence[j], sequence[i]

    # Check if the sequence is sorted after the swap
    for k in range(n - 1):
        if sequence[k] > sequence[k + 1]:
            return True