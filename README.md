## Запуск проекта:  
#### 1. Сщздаем образ из Dockerfile (из коневой директории coolsite)
docker build -t coolsite .
#### 2. Создаем и запускаем контейнер:
docker run --name django-coolsite -p 8000:8000 -d coolsite
