from gendiff.cli import cli
from gendiff.modules.parser import parser_json
from gendiff.modules.diff import generate_diff


def main():
    arg = cli()
    filepath1 = arg.first_file
    filepath2 = arg.second_file
    dict1 = parser_json(filepath1)
    dict2 = parser_json(filepath2)
    diff = generate_diff(dict1, dict2)
    print(diff)



if __name__ == "__main__":
    main()
