def sum_numbers(numbers=None):
    if numbers or numbers == []:
        return sum(numbers)
    return sum(range(1,101))