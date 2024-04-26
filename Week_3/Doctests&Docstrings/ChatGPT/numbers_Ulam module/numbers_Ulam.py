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
    ulam_sequence = [1, 2] if n > 1 else [1]  # Initialize Ulam sequence with first one or two elements
    
    # Generate Ulam sequence up to nth element
    current_number = 3
    while len(ulam_sequence) < n:
        ulam_count = 0  # Counter for number of expressions as sum
        
        # Iterate through existing Ulam sequence to find expressions as sum
        for i in range(len(ulam_sequence)):
            for j in range(i + 1, len(ulam_sequence)):
                if ulam_sequence[i] + ulam_sequence[j] == current_number:
                    ulam_count += 1
                    if ulam_count > 1:  # More than one expression, move to next number
                        break
            if ulam_count > 1:
                break
        
        # If only one expression found, add current_number to Ulam sequence
        if ulam_count == 1:
            ulam_sequence.append(current_number)
        
        current_number += 1  # Move to the next number
    
    return ulam_sequence