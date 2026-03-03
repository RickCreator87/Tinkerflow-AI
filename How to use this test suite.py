How to Use This Test Suite:

1. Install test dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```
2. Run all tests:
   ```bash
   ./run_tests.sh
   ```
3. Run specific test categories:
   ```bash
   # Run only gateway tests
   pytest tests/test_gateway.py -v
   
   # Run only auth tests
   pytest tests/test_auth.py -v
   
   # Run with coverage
   pytest --cov=gateway --cov-report=html
   ```
1. Run tests with markers:
   ```bash
   # Skip integration/slow tests
   pytest -m "not slow and not integration"
   
   # Run only integration tests
   pytest -m integration
```
