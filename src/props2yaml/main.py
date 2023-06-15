#!/usr/bin/env python3

import sys
import argparse
import re
import yaml

from props2yaml.__version__ import __version__


def convert_properties_to_yaml(properties_file):
    properties = {}
    with properties_file as in_file:
        for line in in_file:
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = re.split(r"\s*=\s*", line, maxsplit=1)
                nested_keys = key.split(".")
                nested_dict = properties
                for nested_key in nested_keys[:-1]:
                    nested_dict = nested_dict.setdefault(nested_key, {})
                nested_dict[nested_keys[-1]] = value
    return properties


def main():
    parser = argparse.ArgumentParser(description="Convert .properties files into .yaml.")
    parser.add_argument('-v', '--version', action='version', version="%(prog)s " + __version__)
    parser.add_argument(
        "-i",
        "--input-file",
        type=argparse.FileType("r"),
        help=f"Input properties filename",
        required=True,
    )
    parser.add_argument(
        "-o",
        "--output-file",
        type=argparse.FileType("w"),
        help=f"Output yaml filename",
        required=False,
    )
    args = parser.parse_args()

    converted = convert_properties_to_yaml(properties_file=args.input_file)

    if args.output_file:
        with args.output_file as out_file:
            yaml.dump(converted, out_file, default_flow_style=False)
    else:
        yaml.dump(converted, sys.stdout, default_flow_style=False)


if __name__ == "__main__":
    main()
