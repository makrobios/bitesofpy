import argparse
import operator
from functools import reduce


ops = {'add': operator.add,
       'sub': operator.sub,
       'mul': operator.mul,
       'div': operator.truediv }

def calculator(operation, numbers):
    """TODO 1:
       Create a calculator that takes an operation and list of numbers.
       Perform the operation returning the result rounded to 2 decimal
       places"""
    numbers = (float(num) for num in numbers)
    calculation = reduce(ops[operation], numbers)
    return round(calculation, 2)


def create_parser():
    """TODO 2:
       Create an ArgumentParser object:
       - have one operation argument,
       - have one or more integers that can be operated on.
       Returns a argparse.ArgumentParser object.

       Note that type=float times out here so do the casting in the calculator
       function above!"""
    parser = argparse.ArgumentParser(description="A simple Calculator")
    #parser.add_argument('integers', metavar='N', type=int, nargs='+', help="integers")
    parser.add_argument("-a", "--add", action="store", nargs='+', 
                        help="Sums numbers")
    parser.add_argument("-s", "--sub", action="store", nargs='+', 
                        help="Substracts numbers")
    parser.add_argument("-m", "--mul", action="store", nargs='+', 
                        help="Multiply numbers")
    parser.add_argument("-d", "--div", action="store", nargs='+', 
                        help="Divides numbers")
    return parser 


def call_calculator(args=None, stdout=False):
    """Provided/done:
       Calls calculator with provided args object.
       If args are not provided get them via create_parser,
       if stdout is True print the result"""
    parser = create_parser()

    if args is None:
        args = parser.parse_args()

    # taking the first operation in args namespace
    # if combo, e.g. -a and -s, take the first one
    for operation, numbers in vars(args).items():
        if numbers is None:
            continue

        try:
            res = calculator(operation, numbers)
        except ZeroDivisionError:
            res = 0

        if stdout:
            print(res)

        return res


if __name__ == '__main__':
    call_calculator(stdout=True)

