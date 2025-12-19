#!/bin/bash

# Azure Web App startup script for Chainlit application

echo "Starting LangunanGPT Chainlit application..."

# Install dependencies if needed
pip install -r requirements.txt

# Get port from Azure environment variable (defaults to 8000)
PORT=${PORT:-8000}

echo "Starting Chainlit on port $PORT..."

# Start Chainlit application
chainlit run app.py --host 0.0.0.0 --port $PORT
