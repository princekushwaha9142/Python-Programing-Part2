# Implement simple username & password authentication
user = {
    "username": "admin",
    "password": "1234"
}

name = input("Enter username: ")
pwd = input("Enter password: ")

if name == user["username"] and pwd == user["password"]:
    print("Login successful")
else:
    print("Invalid credentials")