from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List,Optional

app=FastAPI()

#6
class User(BaseModel):
    id:int
    name:str
    age:int
    city:Optional[str]=None
#1
@app.get("/")
def root():
    return{"message": "Welcome to FastAPI"}
 
# #2
@app.get("/about")
def about():
    return{
         "name": "Riya Verma",
        "course": "B.Tech CSE",
        "college": "Sardar Beant Singh State University"
    }

#3
@app.get("/user/{user_id}")
def get_user(user_id:int):
    return {"user_id":user_id}
    
#4
@app.get("/search")
def search(q:str):
    return{"query": q }

#SectionB 5
@app.post("/user")
def create_user(user: User):
    return {
        "name": user.name,
        "age": user.age,
        "city": user.city
    }
#7
users=[]
#a
@app.get("/users")
def  get_users():
    return users

#b
@app.post("/users")
def add_user(user:User):
    users.append(user)
    return {"message":"User added successfully","user":user}


#c
@app.get("/users/{id}")
def get_user_by_id(id:int):
    for user in users:
        if user.id == id:
            return user
    raise
HTTPException(status_code=404, detail="user not found") #anwswer: 8

 #d
@app.put("/users/{id}")
def update_user(id:int,updated_user:User):
    for index, user in enumerate(users):
        if user.id == id:
            users[index]=updated_user
            return  {"message": "User updated", "user": updated_user}
    raise HTTPException(status_code=404, detail="User not found")

#e

@app.delete("/users/{id}")
def delete_user(id:int):
    for index, user in enumerate(users):
        if user.id == id:
            deleted_user= users.pop(index)
            return {"message": "User deleted","user":deleted_user}
        raise HTTPException(status_code=404,details="User not found")