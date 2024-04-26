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
    if len(sequence) < 2:
        return False

    # Find the first occurrence where sequence is not sorted in ascending order
    first_out_of_order = None
    for i in range(len(sequence) - 1):
        if sequence[i] > sequence[i + 1]:
            first_out_of_order = i
            break

    # If all elements are in order
    if first_out_of_order is None:
        return False

    # Find the last occurrence where sequence is not sorted in ascending order
    last_out_of_order = None
    for i in range(len(sequence) - 1, 0, -1):
        if sequence[i] < sequence[i - 1]:
            last_out_of_order = i
            break

    # If there's only one out-of-order pair
    if last_out_of_order - first_out_of_order == 1:
        # Swap the elements
        sequence[first_out_of_order], sequence[last_out_of_order] = sequence[last_out_of_order], sequence[first_out_of_order]
        # Check if the sequence becomes sorted after the swap
        return sequence == sorted(sequence)

    # If there are two out-of-order pairs
    if last_out_of_order is not None and first_out_of_order is not None:
        # Swap the elements
        sequence[first_out_of_order], sequence[last_out_of_order] = sequence[last_out_of_order], sequence[first_out_of_order]
        # Check if the sequence becomes sorted after the swap
        return sequence == sorted(sequence)