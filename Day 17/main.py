class User:
    def __init__(self, name, id):
        print("New User has Been Created..")
        self.username = name
        self.id = id
        self.follower = 0

    def follow(self):
        self.follower += 1


user_1 = User("Adithya","001")

print(user_1.username)
print(user_1.id)
print(user_1.follower)
user_1.follow()
user_1.follow()
print(user_1.follower)



