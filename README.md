# props2yaml
Convert `.properties` files into `.yaml`

## install
```bash
pip install -U props2yaml
p2y --version
```

## usage
 - ```bash
   p2y -i config.properties -o config.yml            # (1)
   ```
 - ```bash
   p2y -i config.properties > config.yml             # (2)
   ```
 - ```bash
   cat config.properties | p2y -i - -o config.yml    # (3)
   ```
 - ```bash
   cat config.properties | p2y -i - > config.yml     # (4)
   ```
