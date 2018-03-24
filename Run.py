import argparse
from sys import argv
import Routes


def RunModelTests():
    print "Run Tests"


def RunAllTests():
    RunModelTests()


def RunServer():
    Routes.Serve()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-t',
        '--test_all',
        action='store_true',
        help='Run all tests',
        default=False
        )
    parser.add_argument(
        '-s',
        '--start_server',
        action='store_true',
        help='Starts the server',
        default=False
        )
    args = parser.parse_args(argv[1:])
    if args.test_all:
        RunAllTests()
    if args.start_server:
        RunServer()
