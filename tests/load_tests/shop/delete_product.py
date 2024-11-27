import time
from locust import HttpUser, TaskSet, task, between


class DeleteProductTaskSet(TaskSet):
    @task
    def delete_product(self):
        slug = "product_1"

        response = self.client.get(f"/product/{slug}/delete/")
        csrftoken = response.cookies['csrftoken']

        self.client.post(
            f"/product/{slug}/delete/",
            data={'csrfmiddlewaretoken': csrftoken},
            headers={'X-CSRFToken': csrftoken}
        )


class WebsiteUser(HttpUser):
    tasks = [DeleteProductTaskSet]
    wait_time = between(1, 5)
