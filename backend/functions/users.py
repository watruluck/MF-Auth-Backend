import os 
from supabase import create_client, Client

def check_email(email: str):

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SECRET_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table("users").select("email").eq("email", email).execute()

    if response.data:
        return True
    else:
        return False

def add_user(email: str, name: str, password: str):

    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SECRET_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table("users").insert({"email": email, "name": name, "password": password}).execute()

    if response.data:
        return True
    else:
        return False

def test_add(email: str, name: str, password: str):
    url: str = os.environ.get("SUPABASE_URL")
    key: str = os.environ.get("SUPABASE_SECRET_KEY")
    supabase: Client = create_client(url, key)

    response = supabase.table("users").insert({"email": email, "name": name, "password": password}).execute()

    return response

