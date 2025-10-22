from fastapi import FastAPI, BackgroundTasks
from functions.users import check_email, test_add
from pydantic import BaseModel
import os 
from functions.email import send_verification_email
from functions.users import add_user, check_email, test_add, update_verification_string
import secrets

app = FastAPI()

class User(BaseModel):
    email: str
    name: str
    password: str
 
@app.post("/signup")
def create_user(user: User):

    if check_email(user.email):
        return -1

    token = secrets.token_urlsafe(16)

    if (update_verification_string(user.email, token) == False):
        return -2

    send_verification_email(user.email, user.name, token)

    if (check_email(user.email)):
        return -1

    else:
        
        response = test_add(user.email, user.name, user.password)
        return response.data

@app.post("/verify/{token}")
def create_user(token: str):
    


# @app.post("/users/")
# def create_user():

# POST username, name, 

# if verified is false, clear after 24 hours? 



# steps for signup

# 1. check if email exists already
# 2. if email exists, "email already in use"
# 3. 