def login_required(func):
    def wrapper(user):
        if user == "Rana":
            return func(user)
        else:
            print("Access Denied")
    return wrapper

@login_required
def dashboard(user):
    print("Welcome to dashboard", user)

dashboard("Rana")
dashboard("Guest")