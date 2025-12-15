from flask import Flask, Blueprint, render_template, request, jsonify
from database import supabase

ApiDBTest = Blueprint("ApiDBTest",__name__)

@ApiDBTest.route("/test", methods=["GET", "POST"])
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