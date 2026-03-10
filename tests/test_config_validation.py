tests/test_config_validation.py
tests/test_config_validation.py

```python
import pytest
from config import load_config
import json

def test_app_config_required_fields():
    config = load_config('app')
    assert 'github' in config
    assert 'app_id' in config['github']
```
