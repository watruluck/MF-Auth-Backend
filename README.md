# MF-Auth-Backend

FastAPI backend for my multi-factor authentication system. Handles user auth with email verification, password resets, facial recognition verification, and includes a chess AI for multi-factor challenges.

## Tech Stack

- **FastAPI** - Main web framework
- **Supabase** - PostgreSQL database for user data
- **SendGrid** - Email verification and password reset emails
- **TensorFlow/Keras** - Facial recognition model (150 epochs trained)
- **python-chess** - Chess engine with minimax algorithm

## Project Structure

```
backend/
├── main.py                          # All API routes and FastAPI app
├── 150_epoch_facial_model.keras     # Pre-trained face detection model
├── modeltraining.py                 # Script to retrain the face model
├── requirements.txt                 # Python dependencies
└── functions/
    ├── chess.py                     # Chess AI (minimax + piece-square tables)
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

### Facial Recognition
- Loads a custom Keras model (trained for 150 epochs) on startup
- Accepts image uploads, resizes to 200x200, normalizes pixel values
- Returns prediction (human vs non-human) with confidence score
- Training code included in `modeltraining.py`

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

Create `.env` file:
```env
SUPABASE_URL=your_url
SUPABASE_SECRET_KEY=your_key
SENDGRID_EMAIL=your_email
SENDGRID_KEY=your_key
```

Install and run:
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Server runs on port 8000 (configurable via PORT env var).