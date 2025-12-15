from flask import Flask, render_template, request, jsonify
from Blueprints.PagesBlueprints import pages
from Blueprints.ApiTestBlueprints import ApiDBTest

# Inicializar Flask
app = Flask(__name__)
app.register_blueprint(pages)
app.register_blueprint(ApiDBTest)

if __name__ == '__main__':
    app.run(debug=True)
