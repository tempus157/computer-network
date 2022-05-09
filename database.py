class Database:
    def __init__(self):
        self.data = []

    def create(self, email, password, name):
        self.data.append({
            "email": email,
            "password": password,
            "name": name
        })

    def find_by_email(self, email):
        for user in filter(lambda item: item["email"] == email, self.data):
            return user
        return None

    def remove_by_email(self, email):
        self.data = filter(lambda item: item["email"] != email, self.data)
