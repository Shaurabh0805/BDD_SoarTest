from locust import HttpUser, TaskSet, task

class LoginUserBehavior(TaskSet):
    @task
    def login(self):
        self.client.post("/client_login", data={
            "email": "user1@example.com",
            "password": "password123"
        })

class StressTest(HttpUser):
    tasks = [LoginUserBehavior]
    min_wait = 500
    max_wait = 1000
    host = "http://127.0.0.1:5000"
