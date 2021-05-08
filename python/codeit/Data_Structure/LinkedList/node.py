class Node:
    """링크드 리스트의 노드 클래스"""
    def __init__(self, data):
        self.data = data # 노드가 저장하는 데이터
        self.next = None # 다음 노드에 대한 레퍼런스

class LinkedList:
    """링크드 리스트 클래스"""
    def __init__(self):
        self.head = None
        self.tail = None

    
    def delete_after(self, previous_node):
        """링크드 리스트 삭제 연산. 주어진 노드 뒤를 삭제"""
        data = previous_node.next.data

        # 지우려는 노드가 taile 노드인 경우
        if previous_node.next is self.tail:
            previous_node.next = None
            self.tail = previous_node
        
        else: # 두 노드 사이를 삭제하는 경우
            previous_node.next = previous_node.next.next
        
        # 삭제한 노드를 리턴
        return data

    
    def insert_after(self, previous_node, data):
        """링크드 리스트 주어진 노드 뒤, 삽입하는 메소드"""        
        new_node = Node(data)

        # 가장 마지막 순서에 삽입하는 경우
        if previous_node is self.tail:
            self.tali.next = new_node
            self.tail = new_node
        
        else:   # 두 노드 사이에 삽입하는 경우
            new_node.next = previous_node.next
            previous_node.next = new_node


    def find_node_at(self, index):
        """링크드 리스트 접근 연산 메소드. 파라미터 인덱스는 항상 있다고 가정함"""
        iterator = self.head

        for _ in range(index):
            iterator = iterator.next
        
        return iterator

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            

    def __str__(self):
        res_str="|"
        # 링크드 리스트 안에 모든 노드를 돌기 위한 변수. 가장 앞의 노드로 일단 정의함
        iterator = self.head
        
        # 링크드 리스트를 순회함
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해줌
            res_str += f"{iterator.data} |"
            iterator = iterator.next    # 다음 노드
        
        return res_str

# 새로운 링크드 리스트 생성
my_list = LinkedList()

# 링크드 리스트에 데이터 추가
my_list.append(2)
my_list.append(3)
my_list.append(5)
my_list.append(7)
my_list.append(11)

print(my_list)

node_2 = my_list.find_node_at(2) # 인덱스 2에 있는 노드 접근
my_list.delete_after(node_2) # 인덱스 2 뒤 데이터 삭제

print(my_list)

my_list.insert_after(node_2, 6) # 인덱스 2 뒤에 6을 삽입

print(my_list)

node_1 = my_list.head
my_list.insert_after(node_1, 9)
print(my_list)

# 링크드 리스트 노드에 접근 (데이터 가져오기)
print(my_list.find_node_at(3).data)

# 링크드 리스트 노드에 접근 (데이터 바꾸기)
my_list.find_node_at(2).data = 13

print(my_list) # 전체 링크드 리스트 출력

iterator_2 = my_list.head

while iterator_2 is not None:
    print(iterator_2.data)
    iterator_2 = iterator_2.next


# 데이터 2, 3, 5, 7, 11을 담는 노드 생성
head_node = Node(2)
node_1 = Node(3)
node_2 = Node(5)
node_3 = Node(7)
tail_node = Node(11)
        
# 노드들을 연결
head_node.next = node_1
node_1.next = node_2
node_2.next = node_3
node_3.next = tail_node

# 노드 순서대로 출력
iterator = head_node

while iterator is not None:
    print(iterator.data)
    iterator = iterator.next
