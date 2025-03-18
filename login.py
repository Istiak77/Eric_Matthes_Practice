class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.login_attempts = 0

    def greet(self, user):
        print(f"Greetings to {user.username}: Hi {user.username}, It's {self.username}")

    def login_count(self):
        print(f"Login count: {self.login_attempts}")

    def incr_login(self):
        self.login_attempts += 1 

    def decr_login(self):
        self.login_attempts -=1

    def reset_login(self):
        self.login_attempts = 0 


user1 = User('Istiak', 'a@b', 'ez')


user1.incr_login()

# user1.decr_login()

# user1.login_count()

#user1.reset_login()

user1.login_count()
