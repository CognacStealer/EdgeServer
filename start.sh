#!/bin/bash
# Activate virtual environment
source "$(dirname "$0")/.venv/bin/activate"

# Go to project root
cd "$(dirname "$0")"

# Run FastAPI server
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
