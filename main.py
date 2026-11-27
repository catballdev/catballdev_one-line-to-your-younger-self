#!/usr/bin/env python3
"""Copy line.txt to entry.txt in the output directory.

Read the single line entry from line.txt (located next to this script)
and write its exact contents (including newline) to entry.txt inside the
output directory. The output directory is determined by the
MAKEFUN_OUTPUT_DIR environment variable, defaulting to /output. The output
file is created with world-readable permissions (0644).
"""
import os
from pathlib import Path

# Read line.txt as binary to preserve exact bytes
# Use __file__ to locate line.txt relative to this script's location
line_txt_path = Path(__file__).resolve().parent / "line.txt"
with open(line_txt_path, "rb") as f:
    content = f.read()

# Determine output directory
output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

# Write entry.txt with world-readable permissions (0644)
output_path = os.path.join(output_dir, "entry.txt")
with open(output_path, "wb") as f:
    f.write(content)
os.chmod(output_path, 0o644)