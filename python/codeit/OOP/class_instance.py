class User:
    # 클래스의 내용 작성 (속성, 행동)
    pass # 아무 내용이 없음

# 같은 클래스로 만들어도 각자는 다른 객체
user1 = User()   # 클래스를 이용한 User 인스턴스를 생성하여 user1에 저장
user2 = User()
user3 = User()


# 속성 추가
# 인스턴스 변수 = 인스턴스가 개인적으로 가지고 있는 속성
user1.name = "jinah"
user1.eamil = "captain@codeit.kr"
user1.password = "12345"

user2.name = "chul"
user2.eamil = "test@codeit.kr"
user2.password = "hello"

user3.name = "mary"
user1.eamil = "test2@codeit.kr"
user1.password = "6789"

# 인스턴스 변수를 출력
print(user1.password)
print(user2.password)