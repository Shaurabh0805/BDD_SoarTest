import requests
import random
import string
from behave import given, when, then

BASE_URL = "http://127.0.0.1:5000"


@given('I have endpoints for registration and login')
def step_impl(context):
    context.register_url = f"{BASE_URL}/client_registeration"
    context.login_url = f"{BASE_URL}/client_login"


@when('I register users with random data')
def step_impl(context):
    context.test_users = []
    for i in range(10):
        full_name = ''.join(random.choices(string.ascii_letters, k=8))
        user_name = ''.join(random.choices(string.ascii_letters, k=5))
        email = f"{user_name}@example.com"
        phone = ''.join(random.choices(string.digits, k=10))
        response = requests.post(context.register_url, data={
            "fullName": full_name,
            "userName": user_name,
            "email": email,
            "password": "password123",
            "phone": phone
        })
        assert response.status_code == 200, f"Registration failed for {email}"
        context.test_users.append({
            "userName": user_name,
            "email": email,
            "password": "password123"
        })


@then('the requests should be processed successfully')
def step_impl(context):
    print("All registration and login requests processed successfully.")


@given('I have a user registration endpoint')
def step_impl(context):
    context.register_url = f"{BASE_URL}/client_registeration"


@then('the registration should succeed')
def step_impl(context):
    print("Registration succeeded")


@given('I have a login endpoint')
def step_impl(context):
    context.login_url = f"{BASE_URL}/client_login"


@when('I login with random user credentials')
def step_impl(context):
    if not context.test_users:
        raise AssertionError("No users available for login testing. Ensure registration is completed first.")

    test_user = random.choice(context.test_users)
    response = requests.post(context.login_url, data={
        "userName": test_user["userName"],
        "email": test_user["email"],
        "password": test_user["password"]
    })
    print(f"Login attempt for {test_user['email']} returned status {response.status_code} with body {response.text}")
    assert response.status_code == 200, f"Login failed for {test_user['email']}"



@then('the login should succeed')
def step_impl(context):
    print("Login succeeded")

@given('I have valid users for login')
def step_impl(context):
    context.test_users = [
        {"email": "user1@example.com", "password": "password123"},
        {"email": "user2@example.com", "password": "password123"}
    ]