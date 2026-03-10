setup.py

```python
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="tinkerflow-ai",
    version="1.0.0",
    author="Tinkerflow",
    author_email="dev@tinkerflow.ai",
    description="Deterministic governance engine for GitHub pull requests",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tinkerflow/tinkerflow-ai",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.9",
    install_requires=[
        "fastapi>=0.104.0",
        "uvicorn>=0.24.0",
        "aiohttp>=3.8.0",
        "pydantic>=2.0.0",
        "python-dotenv>=1.0.0",
    ],
    extras_require={
        "dev": ["pytest", "black", "flake8", "isort", "coverage"],
    },
)
```
