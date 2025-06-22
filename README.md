#  🔍  Gendiff CLI – semantic file difference viewer
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
### Tests and linter status:
[![Github Actions Status](https://github.com/HiKris1801/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/HiKris1801/python-project-50/actions)
[![Python CI](https://github.com/HiKris1801/python-project-50/actions/workflows/build.yml/badge.svg)](https://github.com/HiKris1801/python-project-50/actions/workflows/build.yml)
[![Coverage](https://sonarcloud.io/api/project_badges/measure?project=HiKris1801_python-project-50&metric=coverage)](https://sonarcloud.io/summary/new_code?id=HiKris1801_python-project-50) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=HiKris1801_python-project-50&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=HiKris1801_python-project-50)

A command-line tool that detects and displays the difference between two data structures (JSON or YAML).
Useful for configuration management, debugging, and understanding changes between files.

### Key Features:

* Supports .json, .yml, and .yaml formats
* Stylish, plain and json output
* Detects added, removed, changed, and unchanged values
* Designed for clarity and ease of use

### Diff Calculator demo examples

**1. Flat JSON comparison:**

Shows how gendiff compares two simple JSON files with top-level keys.


[![asciicast](https://asciinema.org/a/JOOwftQoLpgxePwav7tQv4agO.svg)](https://asciinema.org/a/JOOwftQoLpgxePwav7tQv4agO)
---
**2. Flat YAML comparison:**

Demonstrates comparing two basic YAML files with no nested structures.

[![asciicast](https://asciinema.org/a/Vts1EunxaI6JLQEygB5qK1JvZ.svg)](https://asciinema.org/a/Vts1EunxaI6JLQEygB5qK1JvZ)
---
**3. Recursive comparison of JSON and YAML files:**

Example of comparing two deeply nested configuration files in different formats (JSON vs YAML).

[![asciicast](https://asciinema.org/a/zBdCr2DgCPH7n3HjrsVmyW5rz.svg)](https://asciinema.org/a/zBdCr2DgCPH7n3HjrsVmyW5rz)
---
**4. Output in plain format (--format plain):**

Displays differences in a human-readable plain text format, suitable for logs or documentation.

[![asciicast](https://asciinema.org/a/np0Ei5fmCbkCRnvjQuM0JQwP8.svg)](https://asciinema.org/a/np0Ei5fmCbkCRnvjQuM0JQwP8)
---
**5. Output in JSON format (--format json):**

Shows structured output as a JSON object, useful for integration with other tools or pipelines.

[![asciicast](https://asciinema.org/a/4d0UOFMmyYLxd1pq7HvXOykaM.svg)](https://asciinema.org/a/4d0UOFMmyYLxd1pq7HvXOykaM)
---
## Installation and usage

1. Make sure you have Python 3 installed.
2. Clone the repository and install it locally using make:

```sh
git clone https://github.com/HiKris1801/python-project-50.git
cd python-project-50
make install
```
3. Compare two files in JSON, YAML, or a mixed format:
```sh
gendiff <first_file_path> <second_file_path>
```
4. You can specify output formats using the --format (or -f) flag:
```sh
gendiff <file1> <file2> --format <format_type>
```

**Available formats:**

* stylish (default)

* plain

* json

**Examples:**

    gendiff file1.json file2.json --format plain

    gendiff file1.yaml file2.yaml --format json


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Need Help?

Open an [issue](https://github.com/HiKris1801/python-project-50/issues) or message me!

## License
**Free Software**

 [![GitHub stars](https://img.shields.io/github/stars/HiKris1801/python-project-50?style=social)](https://github.com/HiKris1801/python-project-50) 
