@echo off
REM Get the local IP address and display network access info

echo.
echo ============================================================
echo  FoodAI - Network Access Information
echo ============================================================
echo.

REM Get IP address
for /f "tokens=2 delims=:" %%a in ('ipconfig ^| findstr /R "IPv4 Address"') do (
    set "ip=%%a"
    set "ip=!ip:~1!"
)

if defined ip (
    echo ✅ Your IP Address: %ip%
    echo.
    echo Share this link with others:
    echo.
    echo   🔗 http://%ip%:5000
    echo.
    echo ============================================================
    echo.
    echo ℹ️  Make sure:
    echo    1. Your firewall allows port 5000 (see next steps)
    echo    2. You're on the same WiFi network
    echo    3. The Flask server is running (python app_web.py)
    echo.
    echo ============================================================
    echo.
) else (
    echo ❌ Could not find IP address
    echo.
    echo Try this instead:
    echo   1. Open Command Prompt
    echo   2. Type: ipconfig
    echo   3. Look for IPv4 Address
)

pause
