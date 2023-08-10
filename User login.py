print("Welcome the system.")
user_name = "yaren"
user_password = "12345"
number_of_incorrect_login_attempts = 3

while True:
    a = input("user name:")
    b = input("password:")
    if user_name == a and user_password != b:
        print("Incorrect password")
        number_of_incorrect_login_attempts -= 1
    elif user_name != a and user_password == b:
        print("Incorrect user name")
        number_of_incorrect_login_attempts -= 1
    elif user_name != a and user_password != b:
        print("Incorrect user name and password")
        number_of_incorrect_login_attempts -= 1
    else:
        print("Successful login")
        break
    if number_of_incorrect_login_attempts == 0:
        print("Unsuccessful login")
        break
        