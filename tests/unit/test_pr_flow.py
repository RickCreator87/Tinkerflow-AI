tests/integration/test_pr_flow.py

```python
import pytest
from app.webhooks.pull_request import handle_pull_request
from fastapi import Request

@pytest.mark.asyncio
async def test_full_pr_flow():
    # Mock GitHub API responses, webhook payload
    # Call handle_pull_request and verify check run created
    pass
```
