@echo off
setlocal

SET IMAGE_NAME=arsen3d/audioface_module:latest
SET DEST_PATH=src/checkpoints
docker pull %IMAGE_NAME%
echo Creating temporary container from %IMAGE_NAME%...
for /f "tokens=*" %%i in ('docker create %IMAGE_NAME%') do set CONTAINER_ID=%%i

if "%CONTAINER_ID%"=="" (
    echo Error: Failed to create container
    exit /b 1
)

echo Copying files from container...
docker cp %CONTAINER_ID%:/app/checkpoints/ %DEST_PATH%

echo Removing temporary container...
docker rm %CONTAINER_ID%

echo Done!
endlocal