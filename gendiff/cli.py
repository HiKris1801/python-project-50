__all__ = ['cli']
import argparse


def cli():
    parser=argparse.ArgumentParser(description='Compares two configuration files and shows a difference.')
    parser.add_argument("first_file", help="path to the first file")
    parser.add_argument("second_file", help="path to the second file")
    parser.add_argument(
        "-f", "--format",
        help="set format of output",
        default="stylish"
    )
    arg=parser.parse_args()
    return arg
