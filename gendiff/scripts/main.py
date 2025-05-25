from gendiff.cli import cli
from gendiff.modules.parser import parser_json


def main():
    arg = cli()
    filepath1 = arg.first_file
    filepath2 = arg.second_file
    parser_json(filepath1)
    parser_json(filepath2)
    print(parser_json(filepath1))
    print(parser_json(filepath2))


if __name__ == "__main__":
    main()
