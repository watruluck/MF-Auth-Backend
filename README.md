# MF-Auth-Backend

FastAPI backend for my multi-factor authentication system. Handles user auth with email verification, password resets, human face verification, and includes a chess AI for multi-factor challenges.

## Tech Stack

- **FastAPI** - Main web framework
- **Supabase** - PostgreSQL database for user data
- **SendGrid** - Email verification and password reset emails
- **TensorFlow/Keras** - Human face verification model (150 epochs trained)
- **python-chess** - Chess engine with minimax algorithm

## Project Structure

```
.
├── main.py                          # All API routes and FastAPI app
├── requirements.txt                 # Python dependencies
├── .env.example                     # Environment variables template
├── models/
│   ├── 150_epoch_facial_model.keras # Pre-trained face detection model
│   └── modeltraining.py             # Script to retrain the face model
└── functions/
    ├── chess.py                     # Chess AI (alpha-beta pruning + piece-square tables)
    ├── email.py                     # SendGrid email functions
    ├── users.py                     # Supabase user operations
    └── verifyhuman.py               # Face verification using the Keras model
```

## Features Breakdown

### Authentication Flow
- **Signup**: Creates user in Supabase, generates verification token, sends email via SendGrid
- **Login**: Checks credentials and verification status
- **Email Verification**: Token-based verification link sent to user's email
- **Password Reset**: Email-based token system to securely reset passwords

### Human Face Verification
- Loads a custom Keras model (trained for 150 epochs) on startup
- Accepts image uploads, resizes to 200x200, normalizes pixel values
- Returns prediction (human vs non-human) with confidence score
- Training code included in `models/modeltraining.py`

### Chess AI
- Minimax algorithm with alpha-beta pruning
- Uses piece-square tables for positional evaluation
- Material evaluation based on standard chess piece values
- Client specifies FEN position and search depth

## API Endpoints

**Auth**: `/signup`, `/login`, `/verify/{token}`  
**Password**: `/startreset/{email}`, `/resetpassword/{token}/{new_password}`  
**Features**: `/verify-face/`, `/aichessmove`  
**Health**: `/` (GET/HEAD)

## Setup

Copy `.env.example` to `.env` and fill in your credentials:
```bash
cp .env.example .env
```

Install and run:
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Server runs on port 8000 (configurable via PORT env var).