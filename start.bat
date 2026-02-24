@echo off
echo Starting MongoDB in Docker...
docker-compose up -d
echo.
echo MongoDB is starting...
echo Waiting for container to be ready...
timeout /t 5 /nobreak >nul
echo.
echo MongoDB is ready!
echo.
echo Connection Details:
echo - Host: localhost
echo - Port: 27017
echo - Username: admin
echo - Password: password123
echo.
echo To access MongoDB shell, run:
echo docker exec -it mongodb_local mongosh -u admin -p password123 --authenticationDatabase admin
echo.
pause
