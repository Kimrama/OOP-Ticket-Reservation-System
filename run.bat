@echo off

echo preparing source...

python -m pip install --upgrade pip
python -m pip install ttkbootstrap
python -m pip install tk
python -m pip install uvicorn
python -m pip install fastapi

echo calling inprogress...

start "" "client.bat"
start "" "server.bat"

