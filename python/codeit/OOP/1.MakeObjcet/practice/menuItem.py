# MenuItem 클래스 구현
# 인스턴스 변수: name(메뉴 이름), price(메뉴 가격)
# 인스턴스 메소드: __init__(클래스의 모든 인스턴수 변수를 초기화), __str__(인스턴스의 정보를 문자열로 리턴)

class MenuItem:
    # 음식 메뉴를 나타내는 클래스
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name} 가격: {self.price}'


# 메뉴 인스턴스 생성
burger = MenuItem("햄버거", 4000)
coke = MenuItem("콜라", 1500)
fries = MenuItem("후렌치 후라이", 1500)

# 메뉴 인스턴스 출력
print(burger)
print(coke)
print(fries)
