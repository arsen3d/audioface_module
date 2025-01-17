@echo off
setlocal
pip install uv
uv pip install -r requirements.txt
cd src
python .
echo Done!
endlocal