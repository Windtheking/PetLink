from Services.RegisterService import UpploadTheUser
from flask import request, redirect, url_for

def MiddlewareRegistrationValidation():
    username = request.form.get("username")
    password = request.form.get("password")
    email = request.form.get("email")

    print("FORM DATA:", request.form)
    print("USERNAME:", request.form.get("username"))
    print("PASSWORD:", request.form.get("password"))
    print("EMAIL:", request.form.get("email"))

    

    if not username or not password or not email:
        return redirect(url_for('pages.MainRegisterRedirection')), 400
    
    UpploadTheUser(username, password, email)