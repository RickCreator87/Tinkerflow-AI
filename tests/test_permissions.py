tests/test_permissions.py

```python
from app.services.permissions import check_permission

def test_permission_check():
    assert check_permission("checks:write", "create_check_run") == True
    assert check_permission("checks:write", "delete_repo") == False
```
