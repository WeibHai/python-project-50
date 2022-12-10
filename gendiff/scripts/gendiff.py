import argparse
from gendiff import generate_diff


parser = argparse.ArgumentParser(description='''
Compares two configuration files and shows a difference.''')

parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument(
    '-f',
    '--format',
    help='set format of output',
    metavar='FORMAT',
    choices=['plain', 'stylish', 'json'],
    default='stylish')

args = parser.parse_args()


def main():
    print(generate_diff(args.first_file, args.second_file, args.FORMAT))


if __name__ == '__main__':
    main()
