# To-Do List API
Простое веб-приложение для ведения списка дел с REST API и веб-интерфейсом.

- Backend: FastAPI (Python)
- Frontend: HTML + CSS + JavaScript (без фреймворков)
- База данных: PostgreSQL
- Контейнеризация: Docker + Docker Compose

## Возможности

- Добавление, просмотр, редактирование (переключение статуса) и удаление задач
- Данные сохраняются в PostgreSQL
- Доступно с любого устройства в локальной сети
- Запуск в Docker (с поддержкой секретов для пароля БД)

## Запуск
1. Клонируйте репозиторий - git clone https://github.com/wudbills/Project1.git
2. cd todo-app
3. docker compose up --build -d


Проект настроен на автоматическую сборку и публикацию Docker-образа в GitHub Container Registry через GitHub Actions.
Образ доступен по адресу:
ghcr.io/wudbills/project1:latest


![Demonstration](https://github.com/wudbills/Project1/blob/main/Демонстрация.PNG)
