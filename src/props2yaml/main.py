#!/usr/bin/env python3

import argparse
import sys

from props2yaml import __version__
from props2yaml import convert_properties_to_yaml


def main():
    parser = argparse.ArgumentParser(
        prog="props2yaml",
        description="Convert .properties files into .yaml.",
        epilog="Example: %(prog)s config1.properties config2.properties -o config.yml",
    )
    parser.add_argument("-v", "--version", action="version", version="%(prog)s " + __version__)
    parser.add_argument(
        "input_files",
        metavar="INPUT_FILE",
        type=argparse.FileType("r"),
        nargs="*",
        help="Input properties filename. Default stdin.",
        default=[sys.stdin],
    )
    parser.add_argument(
        "-o",
        "--output-file",
        type=argparse.FileType("w"),
        help=f"Output yaml filename. Default stdout.",
        required=False,
        default=sys.stdout,
    )
    args = parser.parse_args()

    with args.output_file as output_file:
        for input_file in args.input_files:
            with input_file as file:
                properties = file.read()
                converted = convert_properties_to_yaml(properties)
                if file.fileno() != 0:
                    output_file.write(f"#{file.name}\n")
                output_file.write(f"{converted}\n")


if __name__ == "__main__":
    main()
