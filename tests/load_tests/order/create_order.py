import time
from locust import HttpUser, TaskSet, task, between


class OrderCreateTaskSet(TaskSet):
    def on_start(self):
        response = self.client.get("/account/login/")
        csrftoken = response.cookies['csrftoken']

        self.client.post("/account/login/", {
            "username": "testuser",
            "password": "testpassword123"
        }, headers={"X-CSRFToken": csrftoken})

    @task
    def create_order(self):
        product_id = 1

        cart_data = {
            'quantity': 1,
            'update': False,
        }

        self.client.post(
            f"/cart/add/{product_id}/",
            data=cart_data,
        )

        response = self.client.get("/orders/create/")
        csrftoken = response.cookies['csrftoken']

        order_data = {
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'john.doe@example.com',
            'address': '123 Main St',
            'postal_code': '12345',
            'city': 'Anytown',
            'csrfmiddlewaretoken': csrftoken,
        }

        self.client.post(
            "/orders/create/",
            data=order_data,
            headers={'X-CSRFToken': csrftoken}
        )


class WebsiteUser(HttpUser):
    tasks = [OrderCreateTaskSet]
    wait_time = between(1, 5)
