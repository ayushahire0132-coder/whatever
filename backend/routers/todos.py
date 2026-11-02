from datetime import datetime
from typing import List, Optional
from fastapi import APIRouter, HTTPException, status
from backend.models import Todo, TodoCreate, TodoUpdate

router = APIRouter(prefix="/todos", tags=["todos"])

# In-memory database simulation for todos
# In a production app, this would be backed by an ORM / Database session.
todos_db = []
id_counter = 1

@router.get("/", response_model=List[Todo])
def list_todos(skip: int = 0, limit: int = 100, completed: Optional[bool] = None):
    """
    Retrieve a list of todos with optional filtering by completion status, skip, and limit.
    """
    filtered_todos = todos_db
    if completed is not None:
        filtered_todos = [t for t in filtered_todos if t.completed == completed]
    return filtered_todos[skip : skip + limit]

@router.post("/", response_model=Todo, status_code=status.HTTP_201_CREATED)
def create_todo(todo_in: TodoCreate):
    """
    Create a new todo item.
    """
    global id_counter
    now = datetime.utcnow()
    new_todo = Todo(
        id=id_counter,
        title=todo_in.title,
        description=todo_in.description,
        completed=todo_in.completed,
        created_at=now,
        updated_at=None
    )
    todos_db.append(new_todo)
    id_counter += 1
    return new_todo

@router.get("/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    """
    Retrieve a specific todo item by its unique ID.
    """
    for todo in todos_db:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with ID {todo_id} not found")

@router.put("/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, todo_in: TodoUpdate):
    """
    Update an existing todo item by its ID.
    """
    for index, todo in enumerate(todos_db):
        if todo.id == todo_id:
            update_data = todo_in.dict(exclude_unset=True)
            
            updated_title = update_data.get("title", todo.title)
            updated_desc = update_data.get("description", todo.description)
            updated_comp = update_data.get("completed", todo.completed)
            
            updated_todo = Todo(
                id=todo.id,
                title=updated_title,
                description=updated_desc,
                completed=updated_comp,
                created_at=todo.created_at,
                updated_at=datetime.utcnow()
            )
            todos_db[index] = updated_todo
            return updated_todo

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with ID {todo_id} not found")

@router.delete("/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_todo(todo_id: int):
    """
    Delete a todo item by its ID.
    """
    for index, todo in enumerate(todos_db):
        if todo.id == todo_id:
            todos_db.pop(index)
            return None
            
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Todo with ID {todo_id} not found")
