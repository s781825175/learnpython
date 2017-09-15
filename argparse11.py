import argparse
import argparse10

parser = argparse.ArgumentParser(parents=[argparse10.parser])

parser.add_argument('--local-arg', action="store_true", default=False)

print(parser.parse_args())
