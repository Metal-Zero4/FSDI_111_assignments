from app.database.user import deactivate_user
from flask import Flask, request
from datetime import datetime

app = Flask(__name__)
VERSION = "1.0.0"

from app.database import user

@app.get("/version")
def get_version():
    out = {}
    out["server_time"] = (
        datetime.now().strftime("%F %H:%M:%S"))
    out ["version"] = VERSION
    return out


@app.post("/users")
def create_user():
    user_data = request.json
    new_id = user.insert(
        user_data.get("first_name"),
        user_data.get("last_name"),
        user_data.get("hobbies")
    )
    out = {"new_id": new_id}
    return out, 201

@app.get("/users")
def get_all_users():
    users = user.scan()
    out = {"users": users}
    return out

@app.get("/users/<int:pk>")
def get_single_user(pk):
    user_record = user.read(pk)
    out = {"user": user_record}
    return out

@app.put("/users/<int:pk>")
def update_user(pk):
    user_data = request.json
    user.update(pk,
    user_data.get("first_name"),
    user_data.get("last_name"),
    user_data.get("hobbies"))

    return "OK", 204

@app.delete("/users/<int:pk>")
def delete_user(pk):
    user.deactivate_user(pk)

    return "OK", 200
    
# FOR UPDATE: An HTTP PUT operation with route: /users/<int:pk>
# FOR DEACTIVATE: An HTTP DELETE operation with route: /users/<int:pk>
