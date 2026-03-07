install.sh

```bash
#!/bin/bash
set -e

echo "Installing Tinkerflow-AI..."

# Check Python version
python_version=$(python3 --version 2>&1 | grep -oP '\d+\.\d+')
if (( $(echo "$python_version < 3.9" | bc -l) )); then
    echo "Error: Python 3.9+ required"
    exit 1
fi

# Install dependencies
pip install -r requirements.txt

# Copy config template if not exists
if [ ! -f config/app.config.json ]; then
    cp config/app.config.example.json config/app.config.json
    echo "Please edit config/app.config.json with your GitHub App credentials"
fi

echo "Installation complete. Run 'make run' to start."
```
