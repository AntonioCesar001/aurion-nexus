FROM python:3.12-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    curl \
    git \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Install python tools
RUN pip install --no-cache-dir \
    structlog \
    rich \
    python-slugify \
    pytest \
    mypy \
    ruff \
    keyring

# Copy project files
COPY . .

# Set environment
ENV PYTHONPATH=/app
ENV PATH="/app/bin:${PATH}"

# Default command
CMD ["aurion", "status"]
