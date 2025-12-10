from flask import Flask, render_template
from supabase import create_client
from dotenv import load_dotenv
import os

# Inicializar Flask
app = Flask(__name__)

# Cargar variables desde .env
load_dotenv()

# Obtener variables desde .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Verificación en consola
print("SUPABASE_URL:", SUPABASE_URL)
print("SUPABASE_KEY cargada:", "✅ Sí" if SUPABASE_KEY else "❌ No")

# Crear cliente Supabase (CONEXIÓN)
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
print("✅ Cliente Supabase creado correctamente")


# ---------- RUTAS ----------
@app.route("/")
def home():
    return render_template('indexx.html')

@app.route("/loginlink")
def home1():
    return render_template('Loginlink.html')

@app.route("/loginpetstore")
def home2():
    return render_template('loginpetstore.html')

@app.route("/petlink")
def home3():
    return render_template('petlink.html')

@app.route("/petstores")
def home4():
    return render_template('petstores.html')

# ---------- RUTA DE PRUEBA ----------
@app.route("/test")
def test():
    data = supabase.table("roles").select("*").execute()
    return data.data  # Solo prueba de conexión

if __name__ == '__main__':
    app.run(debug=True)
