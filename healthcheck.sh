healthcheck.sh

```bash
#!/bin/bash
# Health check script for Docker container

curl -f http://localhost:8080/health || exit 1
```
