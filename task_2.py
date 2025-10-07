import random

def get_numbers_ticket(min, max, quantity):
    """
    Generate a sorted list of unique random numbers within a specified range.
    
    This function simulates selecting lottery ticket numbers by generating
    a specified quantity of unique random integers within the given range
    [min, max], inclusive.
    
    Args:
        min (int): The minimum value in the range (must be >= 1).
        max (int): The maximum value in the range (must be <= 1000).
        quantity (int): The number of unique random numbers to generate.
                    Must be between 1 and the available numbers in range.
    
    Returns:
        list: A sorted list of unique random integers. Returns an empty list
            if any validation fails:
            - If any argument is not an integer
            - If min < 1
            - If max > 1000
            - If min > max
            - If quantity < 1 or quantity > (max - min + 1)
    
    Raises:
        TypeError: If any of the arguments are not integers.
    
    Example:
        >>> get_numbers_ticket(1, 49, 6)
        [4, 15, 23, 28, 37, 41]  # Example output (random)
        
        >>> get_numbers_ticket(10, 20, 5)
        [11, 13, 16, 18, 20]  # Example output (random)
        
        >>> get_numbers_ticket(0, 10, 5)
        []  # min < 1
        
        >>> get_numbers_ticket(10, 5, 3)
        []  # min > max
    """

    if not (isinstance(min, int) and isinstance(max, int) and isinstance(quantity, int)):
        raise TypeError("args must be int")
    
    if min < 1:
        return []
    elif max > 1000:
        return []
    elif min > max:
        return []
    
    available_numbers = max - min + 1
    if quantity < 1 or quantity > available_numbers:
        return []
    
    numbers = random.sample(range(min, max + 1), quantity)
    
    return sorted(numbers)

for test in [[1, 49, 5], [6, 49, 4], [-2, 49, 5], [1, 10000, 5], [1, 2, 100], [1, 2, ""]]:
    print(test[0], test[1], test[2])
    try:
        print(get_numbers_ticket(test[0], test[1], test[2]))
    except Exception as e:
        print(e)
    print("______________")
