# run_tests.sh
#!/bin/bash

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

echo -e "${BLUE}Running AI Gateway Tests${NC}\n"

# Run tests with coverage
echo -e "${BLUE}1. Running unit tests...${NC}"
pytest tests/ -v --tb=short

echo -e "\n${BLUE}2. Running tests with coverage...${NC}"
pytest tests/ --cov=gateway --cov=app --cov-report=term-missing --cov-report=html

echo -e "\n${BLUE}3. Running specific test categories:${NC}"
echo -e "${GREEN}   - Gateway endpoint tests...${NC}"
pytest tests/test_gateway.py -v -k "test_health or test_v1_chat"
echo -e "${GREEN}   - Authentication tests...${NC}"
pytest tests/test_auth.py -v
echo -e "${GREEN}   - Transformation tests...${NC}"
pytest tests/test_request_transformer.py -v

echo -e "\n${BLUE}Test complete!${NC}"
