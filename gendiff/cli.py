__all__ = ['cli']
import argparse

__version__ = '1.0.0'


def cli():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')

    parser.add_argument("first_file", help="path to the first file")
    parser.add_argument("second_file", help="path to the second file")

    parser.add_argument(
        "-f", "--format",
        dest='format_name',
        help="set format of output (default: 'stylish')",
        default="stylish"
    )

    parser.add_argument(
        "-V", "--version",
        action="version",
        version=f"%(prog)s {__version__}",
        help="output the version number"
    )
    arg = parser.parse_args()
    return arg
