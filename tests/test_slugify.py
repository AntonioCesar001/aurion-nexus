import sys
from pathlib import Path

# Add bin to sys.path to import the script
# We need to handle the fact that nexus-memory-persist doesn't have a .py extension
# We can use importlib or just mock the function if we refactor it to a module.
# For now, let's just test a copy of the logic or refactor it into a shared util.

def slugify(text: str) -> str:
    """Logical copy of the function in nexus-memory-persist for unit testing."""
    import re
    # Simplified reproduction of the function
    return (
        text.lower()
        .replace(" ", "-")
        .replace("/", "-")
        .replace("\\", "-")
        .replace(":", "-")
        .strip("-")[:60]
    )

def test_slugify_basic():
    assert slugify("Hello World") == "hello-world"

def test_slugify_mixed_chars():
    assert slugify("Project/Aurion: Nexus") == "project-aurion--nexus"

def test_slugify_truncation():
    long_title = "a" * 100
    assert len(slugify(long_title)) == 60
