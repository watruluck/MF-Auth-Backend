from fastapi import FastAPI, BackgroundTasks
from functions.users import check_email, test_add
from pydantic import BaseModel
import os 
from functions.email import send_email_background

app = FastAPI()

class User(BaseModel):
    email: str
    name: str
    password: str
 
@app.post("/signup")
def create_user(user: User):

    if (check_email(user.email)):
        return -1

    else:
        
        response = test_add(user.email, user.name, user.password)
        return response.data

# ----- email -----
@app.post("/send_email")
async def send_email(to_email: str, background_tasks: BackgroundTasks):
    subject = "Welcome to My App"
    body = "Thanks for signing up!"

    # Run sending in background (so FastAPI doesn’t block)
    background_tasks.add_task(send_email_background, to_email, subject, body)
    return {"message": f"Email will be sent to {to_email}"}


# @app.post("/users/")
# def create_user():

# POST username, name, 

# if verified is false, clear after 24 hours? 



# steps for signup

# 1. check if email exists already
# 2. if email exists, "email already in use"
# 3. 