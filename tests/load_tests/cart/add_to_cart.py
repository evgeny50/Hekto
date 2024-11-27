import time
from locust import HttpUser, TaskSet, task, between


class CartAddTaskSet(TaskSet):
    @task
    def add_to_cart(self):
        product_id = 1

        response = self.client.get(f"/cart/")
        csrftoken = response.cookies['csrftoken']

        cart_data = {
            'quantity': 1,
            'update': False,
        }

        self.client.post(
            f"/cart/add/{product_id}/",
            data=cart_data,
            headers={'X-CSRFToken': csrftoken}
        )


class WebsiteUser(HttpUser):
    tasks = [CartAddTaskSet]
    wait_time = between(1, 5)


if __name__ == "__main__":
    import os

    os.system("locust -f load_test.py")
