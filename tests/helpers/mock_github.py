tests/helpers/mock_github.py

```python
import aiohttp
from unittest.mock import MagicMock

class MockGitHubAPI:
    def __init__(self, token):
        self.token = token

    async def get_pr_diff(self, repo, pull_number):
        return "diff --git a/file.py b/file.py\n..."
```
