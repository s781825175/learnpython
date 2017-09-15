import argparse
import argparse6

parser = argparse.ArgumentParser(parents=[argparse6.parser])

parser.add_argument('--local-arg', action="store_true", default=False)

print(parser.parse_args())
