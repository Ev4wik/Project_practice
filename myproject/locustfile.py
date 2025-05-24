from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  # Ждать от 1 до 3 секунд между задачами

    @task
    def view_home(self):
        self.client.get("/")

    @task
    def view_chart(self):
        self.client.get("/chart/")  # Путь зависит от ваших маршрутов