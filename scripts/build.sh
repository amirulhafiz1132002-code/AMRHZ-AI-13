#!/bin/bash

echo "🔧 Building AMRHZ AI System..."

zip -r AMRHZ-AI-13.zip . -x "*.git*" "__pycache__/*"

echo "✅ ZIP READY: AMRHZ-AI-13.zip"