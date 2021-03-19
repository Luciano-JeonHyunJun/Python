##Python Class ##

#클래스 정의
class Dog:
    def dog(self): #메소드 정의
        print("멍 멍")

dog1 = Dog() #인스턴스 생성
dog1.dog() #메소드 호출

#인스턴스 생성과 메소드 호출하기는 .(마침표) 연산자를 사용합니다


#Cat 클래스 정의

class Cat:
    def cat(self):
        print("야옹 야옹")

cat1 = Cat() #function처럼 호출
cat1.cat()
#한마리 더 만들고 싶다면
cat2 = Cat()
cat2.cat()

#인스턴스 변수 생성 (self를 사용한다)

class Cat:
    def info(self):
        self.name = "나비" #function name  생성
        self.color = "검정색"  #인스턴스 변수명을 name 과 color로 생성함
        print('고양이 이름은', self.name ,'색깔은', self.color)
info = Cat() #인스턴스 생성
info.info() # 인스턴스 메소드 실행

#self
# 클래스 인스턴스를 지칭한다.

class Cat:
    def __init__(self, name = "나비" , color = "흰색"):
        self.name = name
        self.color = color
    def info(self):
        print('고양이 이름은' , self.name , '색깔은' , self.color)
cat1 = Cat("네로","흰색")
cat2 = Cat("미미" , "갈색")

cat1.info()
cat2.info()