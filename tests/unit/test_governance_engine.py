tests/unit/test_governance_engine.py

```python
import pytest
from app.services.governance_engine import run_governance
from app.models.schemas import GovernanceResponse

@pytest.mark.asyncio
async def test_run_governance_basic():
    # Mock dependencies (like fetch_pr_diff) using monkeypatch
    result = await run_governance("test/repo", 1, 123, "opened")
    assert isinstance(result, GovernanceResponse)
    assert result.request_id is not None
    assert len(result.results) > 0
```
