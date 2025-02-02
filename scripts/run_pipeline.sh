#!/bin/bash

# Ensure we are inside the project directory
cd "$(dirname "$0")/.."

# Check if Pipenv is installed
if ! command -v pipenv &> /dev/null
then
    echo "Pipenv not found! Please install it using: python -m pip install --user pipenv"
    exit 1
fi

# Activate the virtual environment and run the pipeline
echo "Running Cryptocurrency Tracker Pipeline..."
python -m pipenv run python run_pipeline.py

# Completion message
echo "Pipeline execution complete!"
