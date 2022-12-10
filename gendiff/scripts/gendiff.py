import argparse
from gendiff.engine import get_result


parser = argparse.ArgumentParser(description='''
Compares two configuration files and shows a difference.''')

parser.add_argument('formatter')
parser.add_argument('first_file')
parser.add_argument('second_file')
parser.add_argument(
    '-f',
    '--format',
    help='set format of output',
    metavar='FORMAT')

args = parser.parse_args()


def generate_diff():
    if args.formatter == 'json':
        get_result(args.first_file, args.second_file, args.formatter)
        print('Разница записанна в файл формата JSON.')
    else:
        print(get_result(args.first_file, args.second_file, args.formatter))


if __name__ == '__main__':
    generate_diff()
