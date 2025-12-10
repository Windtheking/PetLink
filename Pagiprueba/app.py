from flask import Flask, render_template, request, jsonify
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
print("SUPABASE_KEY cargada:", " Sí" if SUPABASE_KEY else "No")

# Crear cliente Supabase (CONEXIÓN)
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)
print("Cliente Supabase creado correctamente")


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

@app.route("/petstore")
def home4():
    return render_template('petstore.html')

@app.route("/test", methods=["GET", "POST"])
def test():

    # Mostrar el formulario HTML
    if request.method == "GET":
        return render_template("test.html")

    # Recibir datos del HTML por POST
    if request.method == "POST":
        data = request.get_json()
        name = data.get("name")

        if not name:
            return jsonify({"error": "El nombre no puede estar vacío"}), 400

        try:
            # --- INSERT EN SUPABASE ---
            result = supabase.table("roles").insert({"name": name}).execute()

            return jsonify({
                "status": "ok",
                "mensaje": "Dato insertado correctamente",
                "data": result.data
            })

        except Exception as e:
            print("ERROR INSERT:", e)
            return jsonify({"error": str(e)}), 500
if __name__ == '__main__':
    app.run(debug=True)
