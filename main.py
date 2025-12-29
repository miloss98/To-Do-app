from fastapi import FastAPI

api = FastAPI()

todos = [
    {
        "id": 1,
        "todo_name": "Barbershop",
        "todo_description": "I need to cut my hair and shorten my beard.",
    },
    {
        "id": 2,
        "todo_name": "Grocery Shopping",
        "todo_description": "Buy vegetables, fruits, and dairy products.",
    },
    {
        "id": 3,
        "todo_name": "Workout",
        "todo_description": "Go to the gym for a cardio session.",
    },
    {
        "id": 4,
        "todo_name": "Finish the movie",
        "todo_description": "Finish watching The Oppenheimer movie.",
    },
]


@api.get('/todos/')
def get_all_todos():
    return todos


@api.get('/todos/{id}')
def get_todo(id: int):
    for todo in todos:
        if todo['id'] == id:
            return todo
    return {'TODO not found'}


@api.post('/todos')
def create_todo(todo: dict):
    new_todo_id = max(todo['id'] for todo in todos ) + 1
    print(new_todo_id) 

    new_todo = {
        "id": new_todo_id,
        "todo_name": todo["todo_name"],
        "todo_description": todo["todo_description"]
    }

    todos.append(new_todo)

    return new_todo 
   
         
