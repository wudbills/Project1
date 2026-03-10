from fastapi import FastAPI, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import List

from database import Todo, get_db, init_db

app = FastAPI(title="To-Do List — PostgreSQL")

app.mount("/static", StaticFiles(directory="static"), name="static")


class TodoCreate(BaseModel):
    title: str


class TodoOut(BaseModel):
    id: int
    title: str
    completed: bool

    class Config:
        from_attributes = True


@app.on_event("startup")
async def startup_event():
    await init_db()          # создаём таблицы при запуске (dev-only)
    print("→ PostgreSQL таблицы готовы")


@app.get("/", response_class=HTMLResponse)
async def root():
    with open("static/index.html", encoding="utf-8") as f:
        return f.read()


@app.get("/api/todos", response_model=List[TodoOut])
async def get_todos(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Todo))
    return result.scalars().all()


@app.post("/api/todos", response_model=TodoOut)
async def create_todo(todo: TodoCreate, db: AsyncSession = Depends(get_db)):
    db_todo = Todo(title=todo.title)
    db.add(db_todo)
    await db.commit()
    await db.refresh(db_todo)
    return db_todo


@app.put("/api/todos/{todo_id}", response_model=TodoOut)
async def toggle_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(Todo).where(Todo.id == todo_id)
    result = await db.execute(stmt)
    todo = result.scalar_one_or_none()

    if not todo:
        raise HTTPException(404, "Задача не найдена")

    todo.completed = not todo.completed
    await db.commit()
    await db.refresh(todo)
    return todo


@app.delete("/api/todos/{todo_id}")
async def delete_todo(todo_id: int, db: AsyncSession = Depends(get_db)):
    stmt = select(Todo).where(Todo.id == todo_id)
    result = await db.execute(stmt)
    todo = result.scalar_one_or_none()

    if not todo:
        raise HTTPException(404, "Задача не найдена")

    await db.delete(todo)
    await db.commit()
    return {"message": "Задача удалена"}
