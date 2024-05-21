class Person:
    # 명사, Property 를 정의할 수 있음
    name = ''
    age = 0
    status = 'sleeping'

    def __init__(self, name, age):   # 이 객체의 초기화 함수
        self.name = name
        self.age = age

    # 메소드 ( 함수 = 행위를 지정하는 동사)
    def speak(self):
        print(f'{self.name}: 안녕하세요.')

    def walk(self):
        print(f'{self.name}: 저는 걸어가는 중입니다.')
        
    def run(self):
        print(f'{self.name}: 저는 뛰어가는 중입니다.')
    
    def motion(self):
        print(f'{self.name}: 나의 상태는 {self.status}입니다.')
        self.status = 'walking'

    def introduce(self):
        print(f'안녕하세요, 저는 {self.name} 이고 {self.age} 살 입니다.')

# 사람(Person) 이라는 객체를 만들고,
# 사람이 할 수 있는 행위(methon) 인 speak 와 walk 를 정의
# 사람이라는 객체를 정의(define) 한 상태...
# 이 객체가 만들어지지도 않은 것...
# 객체의 함수는 첫번째 인자가 self 여야 함.
#   나중에, 필요할 때 객체 자신의 속성 등 필요한 부분에 접근하기 위해서 ...

# 이 객체를 통해서 사람을 만들기
# 객체...만들고자 하는 형태의 프로토타입(원형 Prototype)
alice = Person('Alice',30)    # alice.name = 'Alice' / alice.age = 30 을 초기화 함수를 통해 한번에

alice.speak()
alice.walk()
alice.run()
alice.motion()
alice.motion()

bob = Person('Bob',40)

bob.speak()
bob.walk()
bob.run()
bob.introduce()