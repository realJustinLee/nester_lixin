import sys

from nester_lixin import nester

if __name__ == '__main__':
    print(sys.path)
    nester.print_lol(sys.path)
    nester.print_lol(sys.path, True, 1)
