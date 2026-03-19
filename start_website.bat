echo off
REM Start the FoodAI Website

echo.
echo ============================================================
echo.  🍽️  FoodAI - Smart Food Recommendation Website
echo.
echo ============================================================
echo.

REM Check if venv exists
if not exist "venv\Scripts\activate.bat" (
    echo ❌ Virtual environment not found!
    echo Run: python -m venv venv
    pause
    exit /b 1
)

REM Activate venv and start Flask
echo Starting Flask web server...
echo.
call venv\Scripts\activate.bat
echo ✅ Virtual environment activated

REM Start the web app
echo.
echo ============================================================
echo 🚀 Starting FoodAI Website...
echo ============================================================
echo.
echo 📍 Visit: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
echo ============================================================
echo.

python app_web.py

pause
