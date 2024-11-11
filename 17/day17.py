class User:
    def __init__(self, user_id, username): # inicializar/construtor - criamos valores para os atributos
       self.id = user_id     
       self.username = username
       self.followers = 0 # valor default
       self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


# criando objetos da classe User
user_1 = User("001", "carina")
user_2 = User("002", "jack")

print(user_1.username)
print(user_1.id)

user_1.follow(user_2)
print(user_2.followers)
