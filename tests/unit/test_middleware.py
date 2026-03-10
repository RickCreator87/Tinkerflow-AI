tests/unit/test_middleware.py

```python
from fastapi import Request
from gateway.middleware.auth import verify_github_webhook
import pytest

@pytest.mark.asyncio
async def test_verify_signature():
    # Create mock request with proper signature
    pass
```
