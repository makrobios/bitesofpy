def sum_numbers(numbers=None):
    if numbers and numbers not None:
        return sum(numbers)
    return sum(range(1,101))