import os
import random

import django
from locust import HttpUser, TaskSet, task, between
from django.utils.text import slugify

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()


class UserBehavior(TaskSet):

    def on_start(self):
        response = self.client.get("/account/login/")
        self.csrftoken = response.cookies['csrftoken']

    @task
    def create_product(self):
        self.client.post("/product/create/", {
                "category": 2,
                "tags": [2],
                "name": f"Test Product {random.randint(1, 10000)}",
                "slug": str(slugify(f"Test Product {random.randint(1, 10000)}")),
                "code": f"TP{random.randint(1, 10000)}",
                "description": "This is a test product.",
                "additional_info": "Additional information",
                "price": 710,
                "sale_price": 8,
                "available": True
            }, headers={"X-CSRFToken": self.csrftoken})


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
