const API_BASE = "/api/todos";
const todoList = document.getElementById("todoList");
const input = document.getElementById("todoInput");

async function loadTodos() {
  const res = await fetch(API_BASE);
  const todos = await res.json();
  
  todoList.innerHTML = "";
  todos.forEach(todo => {
    const li = document.createElement("li");
    li.className = todo.completed ? "completed" : "";
    
    const text = document.createTextNode(todo.title);
    li.appendChild(text);

    // Кнопка переключения
    const toggleBtn = document.createElement("button");
    toggleBtn.textContent = todo.completed ? "↺" : "✓";
    toggleBtn.onclick = () => toggleTodo(todo.id);
    li.appendChild(toggleBtn);

    // Кнопка удаления
    const delBtn = document.createElement("button");
    delBtn.textContent = "×";
    delBtn.onclick = () => deleteTodo(todo.id);
    li.appendChild(delBtn);

    todoList.appendChild(li);
  });
}

async function addTodo() {
  const title = input.value.trim();
  if (!title) return;

  await fetch(API_BASE, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ title })
  });

  input.value = "";
  loadTodos();
}

async function toggleTodo(id) {
  await fetch(`${API_BASE}/${id}`, { method: "PUT" });
  loadTodos();
}

async function deleteTodo(id) {
  await fetch(`${API_BASE}/${id}`, { method: "DELETE" });
  loadTodos();
}

// Запуск
loadTodos();
input.focus();

// Добавление по Enter
input.addEventListener("keypress", e => {
  if (e.key === "Enter") addTodo();
});
