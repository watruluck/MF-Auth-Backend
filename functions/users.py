import os 
import bcrypt
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Initialize Supabase client once at module level (reused by all functions)
url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_SECRET_KEY")
supabase: Client = create_client(url, key)

def check_email(email: str):
    """Check if email already exists in database"""
    response = supabase.table("users").select("email").eq("email", email).execute()

    if response.data:
        return True
    else:
        return False

def add_user(email: str, name: str, password: str, token: str):
    """Create new user with bcrypt-hashed password"""
    # Hash password with bcrypt (includes automatic salt generation)
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    
    response = supabase.table("users").insert({"email": email, "name": name, "password": hashed_password.decode('utf-8'), "verification_string": token}).execute()

    if response.data:
        return True
    else:
        return False

def check_password(email: str, password: str):
    """Verify password against stored bcrypt hash"""
    response = supabase.table("users").select("password").eq("email", email).execute()

    if response.data:
        stored_hash = response.data[0]["password"].encode('utf-8')
        # Use bcrypt to securely compare password with hash
        return bcrypt.checkpw(password.encode('utf-8'), stored_hash)
    else:
        return False

def verify_user(token:str):
    """Verify user email exists in database using verification token"""
    response = supabase.table("users").update({"is_verified": True}).eq("verification_string", token).execute()

    if response.data:
        return response.data
    else:
        return False

def check_is_verified(email: str):
    """Check if user's email is verified"""
    response = supabase.table("users").select("is_verified").eq("email", email).execute()

    if response.data and response.data[0]["is_verified"]:
        return True
    else:
        return False

def update_verification_string(email:str, verification_string: str):
    """Update user's verification string for password reset"""
    response = supabase.table("users").update({"verification_string": verification_string}).eq("email", email).execute()

    if response.data:
        return True
    else:
        return False


def get_user_by_email(email: str):
    """Retrieve user data by email"""
    response = supabase.table("users").select("*").eq("email", email).execute()

    if response.data:
        return response.data    
    else:
        return None

def update_password(token: str, new_password: str):
    """Update user's password (with bcrypt hashing)"""
    hashed_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt())
    
    response = supabase.table("users").update({"password": hashed_password.decode('utf-8')}).eq("verification_string", token).execute()

    if response.data:
        return True
    else:
        return False