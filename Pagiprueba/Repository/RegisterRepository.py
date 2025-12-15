from database import supabase

def UpploadTheUser(username, password, email):

    action = supabase.table("users").insert({
        "username": username,
        "password": password,
        "email": email
    }).execute()
    print(action)
