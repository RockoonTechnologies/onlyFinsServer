class User:
    def __init__(self, username, password, email, followers=0, extra={}):
        self.username = username
        self.password = password
        self.email = email

        self.followers = followers

        self.extra = extra

    def jsonify(self):
        return {
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "followers": self.followers,
            "extra": self.extra
        }
    def fromJson(self, data):
        self.username = data["username"]
        self.password = data["password"]
        self.email = data["email"]

        self.followers = data["followers"]

        self.extra = data["extra"]

        return self