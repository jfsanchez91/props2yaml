# props2yaml

Convert `.properties` files into `.yaml`

## install

```bash
pip install -U props2yaml
props2yaml --version
```

## cli usage

- ```bash
   props2yaml config.properties -o config.yml          # (1)
   ```
- ```bash
   props2yaml config.properties > config.yml           # (2)
   ```
- ```bash
   cat config.properties | props2yaml -o config.yml    # (3)
   ```
- ```bash
   cat config.properties | props2yaml > config.yml     # (4)
   ```

## python usage

```python3
from props2yaml import convert_properties_to_yaml

converted = convert_properties_to_yaml("config.prop.value=50")
print(converted)
```
_output:_
```yaml
config:
  prop:
    value: '50'
```
