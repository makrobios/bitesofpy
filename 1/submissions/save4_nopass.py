def sum_numbers(numbers=None):
    if numbers or numbers == None:
        return sum(numbers)
    return sum(range(1,101))