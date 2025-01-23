from locust import HttpUser, TaskSet, task

class RegisterUserBehavior(TaskSet):
    @task
    def register(self):
        self.client.post("/client_registeration", data={
            "fullName": "Test User",
            "userName": "testuser",
            "email": "testuser@example.com",
            "password": "password123",
            "phone": "1234567890"
        })

class LoadTest(HttpUser):
    tasks = [RegisterUserBehavior]
    min_wait = 1000
    max_wait = 2000
    host = "http://127.0.0.1:5000"
