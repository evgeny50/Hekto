from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):

    def on_start(self):
        """ This method is called when a Locust user starts. """
        self.user_login()

    @task(1)
    def user_login(self):
        """ Simulate a user login. """
        response = self.client.get("/account/login/")
        csrftoken = response.cookies['csrftoken']

        self.client.post("/account/login/", {
            "username": "testuser",
            "password": "testpassword123"
        }, headers={"X-CSRFToken": csrftoken})


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 2)
    host = "http://localhost:8000"  # Укажите базовый URL вашего приложения
