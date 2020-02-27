import argparse

parser = argparse.ArgumentParser(description='TRY')
parser.add_argument('-a', '--add', type=float, action="store", nargs="+")
parser.add_argument('-b', '--bdd', type=float, action="store", nargs="+")
#parser.add_argument('integers', metavar='N', type=int, nargs="+" )

print(parser.parse_args(['-a',"10","20","-b","30"]))
