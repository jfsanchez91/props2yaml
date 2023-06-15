import yaml
from props2yaml.converter import convert_properties_to_yaml
from yaml import FullLoader


def test_converter():
    properties = """
    config.props.value=50
    config.key.value=150
    config.key2.value=1000
    key=0
    key2=1
    config.key3.value.value2="abc"
    """
    converted = convert_properties_to_yaml(properties)
    yml = yaml.load(converted, Loader=FullLoader)
    assert yml is not None
    assert yml["config"]["props"]["value"] == "50"
    assert yml["config"]["key"]["value"] == "150"
    assert yml["config"]["key2"]["value"] == "1000"
    assert yml["key"] == "0"
    assert yml["key2"] == "1"
    assert yml["config"]["key3"]["value"]["value2"] == '"abc"'
