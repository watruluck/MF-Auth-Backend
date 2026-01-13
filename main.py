from fastapi import FastAPI, BackgroundTasks, File, UploadFile
from pydantic import BaseModel
import os 
from functions.email import send_verification_email, send_password_reset_email
from functions.users import add_user, check_email, update_verification_string, verify_user, check_password, check_is_verified, get_user_by_email, update_password
import secrets
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from functions.chess import get_bot_move
from functions.verifyhuman import verify_human
from tensorflow import keras
from contextlib import asynccontextmanager

# Load model at startup
model = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    global model
    model_path = os.path.join(os.path.dirname(__file__), 'functions/../models/150_epoch_facial_model.keras')
    model = keras.models.load_model(model_path)
    yield
    model = None

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class User(BaseModel):
    email: str
    name: str
    password: str

class LoginUser(BaseModel):
    email: str
    password: str

class Board(BaseModel):
    fen: str
    depth: int

@app.get("/")
@app.head("/")
def health_check():
    return {"status": "ok", "message": "MF-Auth Backend is running"}
 
@app.post("/signup")
def create_user(user: User):
    if check_email(user.email):
        return -1

    token = secrets.token_urlsafe(16)
    if not add_user(user.email, user.name, user.password, token):
        return -2

    if not send_verification_email(user.email, user.name, token):
        return -3

    return 0

@app.post("/login")
def login_user(user: LoginUser):

    if not check_email(user.email):
        return -1

    if check_password(user.email, user.password) == False:
        return -2

    if not check_is_verified(user.email):
        return -3

    return 0

@app.post("/verify/{token}")
def verify_email(token: str):
    response = verify_user(token)

    if not response:
        return -1
    else:
        return JSONResponse(content={"name": response[0]["name"], "email": response[0]["email"]})

@app.post("/startreset/{email}")
def start_password_reset(email: str):

    if not check_email(email):
        return -1
    
    user = get_user_by_email(email)

    if not user:
        return -2

    response = send_password_reset_email(email, user[0]["name"], user[0]["verification_string"])

    if not response:
        return -3
    else:
        return JSONResponse(content={"name": user[0]["name"], "email": user[0]["email"]})

@app.post("/resetpassword/{token}/{new_password}")
def reset_password(token: str, new_password: str):

    response = update_password(token, new_password)

    if response:
        return 0
    else:
        return -1

@app.post("/aichessmove")
def get_ai_chess_move(board: Board):

    response = get_bot_move(board.fen, board.depth)

    if response:
        return JSONResponse(content={"fen": response})
    else:
        return JSONResponse(content={"error": "Failed to get move"}, status_code=400)


@app.post("/verify-face/")
async def verify_face(file: UploadFile = File(...)):
    contents = await file.read()

    result = await verify_human(contents, model)

    return result

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=False)