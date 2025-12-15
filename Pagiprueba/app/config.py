import os
from dotenv import load_dotenv

# Cargar variables desde .env
load_dotenv()

class config():
    """
        This block of code its meant to have the middle point for the 
        enveriment variables, in other words this recovers the values of the enviromental
        variables and send them to where it is improted, this is in order to have indirectly protected
        the supabase variables and to have more organization using the repository architecture
    """
    SUPABASE_URL = os.getenv("SUPABASE_URL")
    SUPABASE_KEY = os.getenv("SUPABASE_KEY")