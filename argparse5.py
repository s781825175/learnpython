import argparse
parser = argparse.ArgumentParser(prog='PROG')

parser.add_argument('-v', '--version', action='version', version='%(prog)s 1.0')
parser.add_argument('-a', action="store_true", default=False)
parser.add_argument('-b', action="store", dest="b")
parser.add_argument('-c', action="store", dest="c", type=int)

print(parser.parse_args())
print('this is not print')
