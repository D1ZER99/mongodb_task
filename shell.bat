@echo off
echo Connecting to MongoDB shell...
echo.
docker exec -it mongodb_local mongosh -u admin -p password123 --authenticationDatabase admin
