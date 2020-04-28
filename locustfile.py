from locust import HttpLocust, TaskSet, between, task

def login(l):
    l.client.post("/login/", {"usuario":"omaurtorsac", "password":"abcd.1234"})

def index(l):
    l.client.get("")

def logout(l):
    l.client.get("/logout/", {"usuario":"omaurtorsac", "password":"abcd.1234"})

class UserBehavior(TaskSet):
    tasks = {index: 2}

    def on_start(self):
        login(self)

    def on_stop(self):
        logout(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(5.0, 9.0)
