from app.config import config
from supabase import create_client
from flask import abort


"""
    This fragment of code is meant to have the conection to the database made,
    following the repository architecture, we know in the repository only goes 
    the direct interactions with the database and the interaction with the database
    as this is the only program that is directly related to the database

"""
print("SUPABASE_URL:",config.SUPABASE_URL)
print("SUPABASE_KEY cargada:", " Sí" if config.SUPABASE_KEY else "No")
try:
    supabase = create_client(config.SUPABASE_URL, config.SUPABASE_KEY)
except ValueError as e:
   abort(status_code=500, detail=f"Error interno del servidor al inicializar Supabase: {str(e)}")