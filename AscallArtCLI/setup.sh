#!/bin/bash
# -*- coding: utf-8 -*-
# Copyright (c) 2025
# By : Mohammed Al-Baqer

set -e

echo "[Virtual Environment Setup]"

# Detect Operating System
OS=$(uname -s)

# Create Virtual Environment
python3 -m venv venv

# Activate Virtual Environment
source venv/bin/activate

# Dry-run installation (test only)
pip install --dry-run -r requirements.txt

echo ""
echo "Virtual Environment created successfully"
echo "[Starting Installation]"
echo ""

if [[ "$OS" == "Linux" ]]; then
    # Install with --break-system-packages (⚠ risky)
    pip install -r requirements.txt --break-system-packages
elif [[ "$OS" == "Darwin" ]]; then
    # Darwin = macOS
    pip install -r requirements.txt
else
    echo "⚠ Unsupported OS detected: $OS"
    echo "Proceeding with normal installation..."
    pip install -r requirements.txt
fi

echo ""
echo "[Installation Completed]"
