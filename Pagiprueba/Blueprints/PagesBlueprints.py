from flask import Flask, Blueprint, render_template, request, jsonify
from Controllers.UsserRegisterController import MiddlewareRegistrationValidation

pages = Blueprint("pages",__name__)


@pages.route("/")
def home():
    return render_template('indexx.html')

@pages.route("/loginlink")
def home1():
    return render_template('LogedIn/Loginlink.html')

@pages.route("/loginpetstore")
def home2():
    return render_template('LogedIn/loginpetstore.html')

@pages.route("/petlink")
def home3():
    return render_template('NotLogedIn/petlink.html')

@pages.route("/petstore")
def home4():
    return render_template('NotLogedIn/petstores.html')

@pages.route("/Register")
def MainRegisterRedirection():
    return render_template('Register.html')

@pages.route("/RegisterMiddlestep", methods = ["GET", "POST"])
def MiddlewareRegistration():
    MiddlewareRegistrationValidation()
    return render_template('LogedIn/Loginlink.html')