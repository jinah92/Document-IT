# name, email, method를 한번에 초기화하는 메소드 만들기
class User:
    count = 0 # 모든 인스턴스의 개수

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        User.count += 1

    def __str__(self):
        return f"사용자: {self.name}, 이메일: {self.email}"


    def __repr__(self) -> str:
        return f"사용자: {self.name}, 이메일: {self.email}"


    @classmethod    # 클래스 메소드
    def number_of_users(cls):
        # cls.count == User.count
        print(f'총 유저의 수는 {cls.count}입니다.')
        


# 1. 인스턴스 생성
# 2. init 메서드 자동 호출
user1 = User("Young", "young@codeit.kr", "123456")

user2 = User("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")

user3 = User("Taeho", "taeho@codeit.kr", "123abc")

user4 = User("Lisa", "lisa@codeit.kr", "abc123")


print(user1.name, user1.email, user1.password)
print(user2.name, user2.email, user2.password)
print(user3.name, user3.email, user3.password)
print(user4.name, user4.email, user4.password)

print(user1)
print(user2)
print(user3)
print(user4)

print(User.count)

User.number_of_users()  # 클래스가 첫번째 인자로 자동 전달
user1.number_of_users()