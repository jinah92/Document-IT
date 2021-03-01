from class_instance import User

user1 = User()

user1.name = "jinah"
user1.email = "captain@codeit.kr"
user1.password = "12345"

User.say_hello(user1)
user1.say_hello()
# user1.say_hello(user1) # error

user1.login("jinah", "captain@codeit.kr")
