class User:
    def __init__(self):
        self.users = {}

    def register(self, username, password):
        if username in self.users:
            return "Użytkownik już istnieje!"
        self.users[username] = password
        return "Rejestracja udana!"

    def login(self, username, password):
        if self.users.get(username) == password:
            return "Zalogowano pomyślnie!"
        return "Błędne dane logowania!"

konto = User()
print(konto.register("jan", "haslo123"))
print(konto.login("jan", "haslo123"))
