import bcrypt
import jwt


class Database:
    def __init__(self):
        self._users = []

    def create(self, email, password, name):
        self._users.append({
            "email": email,
            "password": bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()),
            "name": name,
        })

    def find_by_email(self, email):
        for user in filter(lambda item: item["email"] == email, self._users):
            return user
        return None

    def find_by_credential(self, credential, secret):
        try:
            email = jwt.decode(credential, secret, algorithms="HS256")["email"]
        except jwt.exceptions.DecodeError:
            return None
        return self.find_by_email(email)

    def remove_by_email(self, email):
        self._users = filter(lambda item: item["email"] != email, self._users)

    def print(self):
        print("[")
        for user in self._users:
            print("  {")
            for key, value in user.items():
                print(f"    {key}: {value}")
            print("  },")
        print("]")
