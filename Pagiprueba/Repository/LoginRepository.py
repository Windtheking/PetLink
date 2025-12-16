from database import supabase

def get_user_by_credentials(email, password):
    response = (
        supabase
        .table("users")
        .select("email, password")
        .eq("email", email)
        .eq("password", password)
        .single()
        .execute()
    )

    return response.data