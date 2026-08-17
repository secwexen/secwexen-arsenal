#!/bin/bash

echo "=== Secwexen Arsenal Demo ==="

echo "[1] Checking project..."
[ -d "tools" ] && echo "Tools found."

echo "[2] Running defensive demo..."
python -m demo/defensive_demo.py

echo "[3] Running tests..."
pytest tests/

echo "=== Demo Complete ==="
