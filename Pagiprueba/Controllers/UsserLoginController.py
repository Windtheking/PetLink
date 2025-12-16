from flask import request
from Services.LoginService import login_user


def Usserlogin():
    email = request.form.get("email")
    password = request.form.get("password")

    Information = login_user(email, password)

    if Information:
        var = True
        return var
    elif not Information:
        var = False
        return "<h1>te equivocaste</h1>"
    

