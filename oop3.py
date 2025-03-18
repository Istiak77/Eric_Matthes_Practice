class User:
    def __init__(self, username, email, password):
        self.username = username
        self.emali = email
        self.password = password

    def greet(self, user):
        print(f"Grettings to {user.username}: Hi {user.username}, It's {self.username}")


user1 = User("Istiak","mail@mail.com","123")
user2 = User("Adil","maill@mail.com","321")

user1.greet(user2)