def sum_numbers(numbers=None):
    if numbers and numbers == None:
        return sum(numbers)
    return sum(range(1,101))