import argparse
from sys import argv
import Routes
import Database


def RunServer():
    Database.Initialize()
    Routes.Serve()


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-s',
        '--start_server',
        action='store_true',
        help='Starts the server',
        default=False
        )
    args = parser.parse_args(argv[1:])
    if args.start_server:
        RunServer()
