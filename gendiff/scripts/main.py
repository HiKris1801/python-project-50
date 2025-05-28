from gendiff.cli import cli
from gendiff.modules.parser import parser_json
#from gendiff.modules.diff import generate_diff


def main():
    arg = cli()
    filepath1 = arg.first_file
    filepath2 = arg.second_file
    parser_json(filepath1)
    parser_json(filepath2)
    #generate_diff(filepath1, filepath2)
    #print(generate_diff())
    #print(parser_json(filepath2))


if __name__ == "__main__":
    main()
