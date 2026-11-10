# Q4. Design a reusable Login class using OOP
# Intermediate
# Scenario: You are building a reusable Python automation framework. Multiple test scripts need to validate login credentials.
#
# Create a Login class.
#
# Input:
# login = Login("admin", "admin123")print(login.authenticate("admin", "admin123"))print(login.authenticate("admin", "wrong123"))
#
#
#
# Expected output:
# True
# False
#
#
# Requirements:
# 1. Create a class named Login.
# 2. Initialize username and password through the constructor.
# 3. Store credentials as private instance attributes.
# 4. Create an authenticate() method.
# 5. Return True for valid credentials and False otherwise.
# 6. Do not print results inside the method.
# Edge cases:
# - Empty username.
# - Empty password.
# - Incorrect username.
# - Incorrect password.
# Expected deliverable: Complete Python class with two test calls.
class Login:

    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def authenticate(self, username, password):

        if username == self.__username and password == self.__password:
            return True
        else:
            return False


# Create object
login = Login("admin", "admin123")

# Test valid credentials
print(login.authenticate("admin", "admin123"))

# Test invalid credentials
print(login.authenticate("admin", "wrong123"))