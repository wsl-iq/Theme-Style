:: batchfile/bin/bash
:: -*- coding: utf-8 -*-
:: Copyright (c) 2025
:: By : Mohammed Al-Baqer

@echo off
REM Creation Virtual Environment
python -m venv venv
REM Activate Virtual Environment
call venv\Scripts\activate
REM Install libraries from requirements.txt
pip install --dry-run -r requirements.txt
echo.
echo successfully created virtual environment and activated it.
echo.
echo Installing libraries...
echo.
pip install -r requirements.txt
echo Installation completed successfully 
pause
