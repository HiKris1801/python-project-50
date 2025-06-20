import sys

from gendiff.cli import cli


def test_cli_arguments(monkeypatch):
    test_args = ['gendiff', 'file1.json', 'file2.json', '--format', 'plain']
    monkeypatch.setattr(sys, 'argv', test_args)

    args = cli()
    assert args.first_file == 'file1.json'
    assert args.second_file == 'file2.json'
    assert args.format_name == 'plain'


def test_cli_arguments_default_format(monkeypatch):
    test_args = ['gendiff', 'file1.json', 'file2.json']
    monkeypatch.setattr(sys, 'argv', test_args)

    args = cli()
    assert args.format_name == 'stylish'
