from Repository.LoginRepository import get_user_by_credentials

def login_user(email, password):
    user = get_user_by_credentials(email, password)

    return user