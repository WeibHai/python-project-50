import argparse
from gendiff import generate_diff


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


def main():
    if args.formatter == 'json':
        generate_diff(args.first_file, args.second_file, args.formatter)
        print('Разница записанна в файл формата JSON.')
    else:
        print(generate_diff(args.first_file, args.second_file, args.formatter))


if __name__ == '__main__':
    main()
