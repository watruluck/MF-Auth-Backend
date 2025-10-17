from fastapi import FastAPI, BackgroundTasks
from functions.users import check_email, test_add
from pydantic import BaseModel
import os 
from functions.email import send_verification_email

app = FastAPI()

class User(BaseModel):
    email: str
    name: str
    password: str
 
@app.post("/signup")
def create_user(user: User):

    send_verification_email("watruluck@gmail.com", "Will T")

    if (check_email(user.email)):
        return -1

    else:
        
        response = test_add(user.email, user.name, user.password)
        return response.data


# @app.post("/users/")
# def create_user():

# POST username, name, 

# if verified is false, clear after 24 hours? 



# steps for signup

# 1. check if email exists already
# 2. if email exists, "email already in use"
# 3. 