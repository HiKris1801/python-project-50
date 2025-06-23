from gendiff.cli import cli
from gendiff.modules.diff import generate_diff


def main():
    arg = cli()
    filepath1 = arg.first_file
    filepath2 = arg.second_file

    result_format = generate_diff(
        filepath1,
        filepath2,
        format_name=arg.format_name,
    )
    print(result_format)


if __name__ == "__main__":
    main()
