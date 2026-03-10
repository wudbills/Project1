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
1. Клонируйте репозиторий - git clone https://github.com/ВАШ-ЮЗЕРНЕЙМ/todo-app.git
   cd todo-app
2. docker compose up --build -d


Проект настроен на автоматическую сборку и публикацию Docker-образа в GitHub Container Registry через GitHub Actions.
Образ доступен по адресу:
ghcr.io/wudbills/project1:sha-a0520ee


![Demonstration](https://github.com/wudbills/Project1/blob/main/Демонстрация.PNG)
