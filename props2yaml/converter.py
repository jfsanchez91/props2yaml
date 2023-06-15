import re
import yaml

__all__ = [
    "convert_properties_to_yaml",
]


def convert_properties_to_yaml(properties: str) -> str:
    converted = {}
    for line in properties.split("\n"):
        line = line.strip()
        if line and not line.startswith("#"):
            key, value = re.split(r"\s*=\s*", line, maxsplit=1)
            nested_keys = key.split(".")
            nested_dict = converted
            for nested_key in nested_keys[:-1]:
                nested_dict = nested_dict.setdefault(nested_key, {})
            nested_dict[nested_keys[-1]] = value
    return yaml.dump(converted, stream=None, default_flow_style=False)
