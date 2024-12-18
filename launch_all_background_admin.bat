@echo off
powershell Start-Process pythonw -ArgumentList "temperature_server.py" -WorkingDirectory "%cd%" -WindowStyle Hidden -Verb RunAs
timeout /t 2 /nobreak > nul
powershell Start-Process pythonw -ArgumentList "app.py" -WorkingDirectory "%cd%" -WindowStyle Hidden -Verb RunAs
exit
