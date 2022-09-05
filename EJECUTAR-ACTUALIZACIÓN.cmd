@echo off
setlocal

set BASEDIR=%~dp0

cd %BASEDIR%

echo "-----------------------------------------------------"
echo "Starting Bonita Tomcat bundle"
echo "-----------------------------------------------------"
call python UPDATE_CERTIFICADOS.py

echo "-----------------------------------------------------"
echo "Starting Bonita Tomcat bundle"
echo "-----------------------------------------------------"

exit /b 0

:exit
:: pause to let the user read the error message:
pause
exit /b 1