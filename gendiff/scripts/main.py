from gendiff.cli import cli
from gendiff.formatters.stylish import format_stylish
from gendiff.modules.diff import generate_diff
from gendiff.modules.file_extension import get_file_extension
from gendiff.modules.parser_by_extension import get_parser_by_extension


def main():
    arg = cli()
    filepath1 = arg.first_file
    filepath2 = arg.second_file
    ext1 = get_file_extension(filepath1)
    ext2 = get_file_extension(filepath2)
    parser1 = get_parser_by_extension(ext1)
    parser2 = get_parser_by_extension(ext2)

    dict1 = parser1(filepath1)
    dict2 = parser2(filepath2)
    diff_tree = generate_diff(dict1, dict2)
    result_format = format_stylish(diff_tree)
    print(result_format)


if __name__ == "__main__":
    main()
