from locust import HttpUser, TaskSet, task, between


class EditProductTaskSet(TaskSet):
    @task
    def edit_product(self):
        slug = "product_1"

        response = self.client.get(f"/product/{slug}/edit/")
        csrftoken = response.cookies['csrftoken']

        product_data = {
            'name': 'Updated Product Name',
            'description': 'Updated product description',
            'price': '99.99',
            'csrfmiddlewaretoken': csrftoken,
        }

        self.client.post(
            f"/product/{slug}/edit/",
            data=product_data,
            headers={'X-CSRFToken': csrftoken},
            files={}
        )


class WebsiteUser(HttpUser):
    tasks = [EditProductTaskSet]
    wait_time = between(1, 5)
