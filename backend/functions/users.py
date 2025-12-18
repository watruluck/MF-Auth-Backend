import os 
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

def check_email(email: str):

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SECRET_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table("users").select("email").eq("email", email).execute()

    if response.data:
        return True
    else:
        return False

def add_user(email: str, name: str, password: str, token: str):

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SECRET_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table("users").insert({"email": email, "name": name, "password": password, "verification_string": token}).execute()

    if response.data:
        return True
    else:
        return False

def check_password(email: str, password: str):
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SECRET_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table("users").select("password").eq("email", email).execute()

    if response.data and response.data[0]["password"] == password:
        return True
    else:
        return False

def verify_user(token:str):
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SECRET_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table("users").update({"is_verified": True}).eq("verification_string", token).execute()

    if response.data:
        return response.data
    else:
        return False

def check_is_verified(email: str):
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SECRET_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table("users").select("is_verified").eq("email", email).execute()

    if response.data and response.data[0]["is_verified"]:
        return True
    else:
        return False

def update_verification_string(email:str, verification_string: str):
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SECRET_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table("users").update({"verification_string": verification_string}).eq("email", email).execute()

    if response.data:
        return True
    else:
        return False


def get_user_by_email(email: str):
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SECRET_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table("users").select("*").eq("email", email).execute()

    if response.data:
        return response.data    
    else:
        return None

def update_password(token: str, new_password: str):
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SECRET_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table("users").update({"password": new_password}).eq("verification_string", token).execute()

    if response.data:
        return True
    else:
        return False