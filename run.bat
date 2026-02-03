@echo off
cd /d "%~dp0"
echo.
echo ========================================
echo   Car Dodge Game - Build Script
echo ========================================
echo.

echo Compiling Java files...
javac -d out src\GameEngine.java src\GameServer.java

if %ERRORLEVEL% EQU 0 (
    echo.
    echo ✓ Compilation successful!
    echo.
    echo ========================================
    echo   Starting Game Server...
    echo ========================================
    echo.
    echo Game server is running on: http://localhost:8000
    echo Open your browser to play the game!
    echo.
    echo Controls:
    echo - Arrow Left/Right or A/D to move
    echo - Press Ctrl+C to stop the server
    echo.
    
    java -cp out GameServer
) else (
    echo.
    echo ✗ Compilation failed! Please check the errors above.
    pause
)
