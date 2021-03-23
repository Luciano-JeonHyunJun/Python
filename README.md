# Python
파이썬 기초를 코드로 정리하는 커밋입니다.  / It's a commit that cleans up the Python basics into code.

<h1>global 지역변수 전역변수 2021.3.17</h1>
지역변수와 전역변수는  변수의 유효한 범위를 기준으로 구분할때 사용하는 변수명입니다.<br>

<ol>
  <li>지역변수: 함수 안에서만 유효한 변수입니다.</li>
  
  <li>전역변수: 코드 전체에서 유효한 변수입니다.</li>
  
</ol>
<br>
그래서 지역변수를 선언하는 위치는 함수 내부가 됩니다, 그러면 반대로 전역변수는 함수 바깥이구요.<br>
지역변수는 function을 벗어나면 더 이상 유효하지 않습니다. 함수의 Argument로 선언된 변수는 함수 내에서만 
유효한 지역변수입니다.

<br>

만약 함수 안에서 선언한 지역변수와 밖에서 선언한 전역변수가 이름이 같다면 어떤 방법을 써야할까요? <br><br>
-함수 안에서 선언한 지역변수가 함수 밖에서 선언된 전역변수와 이름이 같다면 
 함수 내에서는 '지역변수'(함수 안에서 우선)이기때문에 지역변수로 취급이 됩니다.

-함수 안에서 밖에서 선언한 지역변수를 이용하려면 <strong>"global"</strong>키워드를 사용하면 됩니다.

<h2>코드 해석</h2>
1~2줄은 함수밖에서 param과 strdata를 50과 '전역변수'라고 지정했습니다<br><br>
4~6줄은 strdata에 '지역변수'라는 string을 대입 strdata는 func1안에 있으니 함수 내부에서 선언되었으니 , '지역변수'가 되고 func1을 벗어나면
유효한 변수가 아니게 됩니다.<br><br>
8~9줄은 func2는 param이라는 한개의 Argument를 가지고 있습니다. Argument이름은 param은 전역변수와 이름이 같지만 func2 내에서만 유효한 지역변수입니다.
따라서 func2()내에서 아무리 param에 값을 대입해도 전역변수 param은 영향을 받지 않습니다.(즉 이름만 같은 동명이인 같은것입니다.)<br><br>
11~13줄은 func3 내부에서 global을 사용하여 전역변수로 선언된 param을 사용할 것임을 선언했습니다.
이제 func3의 param은 전역변수(코드전체에서 유효한) 을 이용하는것이므로 값을 변경하면 현재 값도 변경이 됩니다.<br><br>
15~16줄은 func1을 호출하면 func1내에서 선언한 지역변수 strdata값인 '지역변수'(함수 안에서만 유효)
하지만 전역변수(코드 전체에서 유효한)출력하면 '전역변수'(코드 전체에서 유효한)가 출력됩니다.<br>

# Python(ENGver) 
<h4>Please inform that all translations have been made through Google Translator.</h4>
It is a commit that cleans up the Python basics into code. / It's a commit that cleans up the Python basics into code.

<h1>global local variable global variable 2021.3.17</h1>
Local and global variables are variable names that are used when classifying them based on the valid range of the variable.<br>

<ol>
  <li>Local variable: This is a variable that is only valid inside a function.</li>
  
  <li>Global variable: This is a valid variable throughout the code.</li>
  
</ol>
<br>
So, the place where local variables are declared is inside the function, and on the contrary, global variables are outside the function.<br>
Local variables are no longer valid after leaving a function. Variables declared as function Argument are only within the function.
This is a valid local variable.

<br>

If a local variable declared in a function and a global variable declared outside have the same name, what method should be used? <br><br>
-If the local variable declared in the function has the same name as the global variable declared outside the function
 In a function, it is treated as a local variable because it is a'local variable' (priority in the function).

-If you want to use local variables declared outside of the function, you can use the keyword <strong>"global"</strong>.

<h2>Code interpretation</h2>
Lines 1~2 specify 50 and'global variable' for param and strdata outside the function.<br><br>
Lines 4~6 assign a string called'local variable' to strdata. Since strdata is in func1, it is declared inside the function, so when it becomes'local variable' and leaves func1
It will not be a valid variable.<br><br>
Lines 8~9, func2 has one argument called param. Argument name param has the same name as global variable, but is a local variable that is only valid within func2.
Therefore, no matter how much you assign a value to param in func2(), the global variable param is not affected (that is, the same name is the same name).<br><br>
Lines 11-13 declared that we will use the param declared as a global variable by using global inside func3.
Now, the param of func3 is to use a global variable (valid throughout the code), so if you change the value, the current value is also changed.<br><br>
Lines 15~16 are'local variable', which is the local variable strdata value declared in func1 when func1 is called (valid only inside a function)
However, when outputting a global variable (valid throughout the code),'global variable' (valid throughout the code) is displayed.<br>

<h1>Class 정의와 self 2021.03.19</h1>

<h1>Class</h1><br>
클래스를 사용하는 이유는 간단합니다 .  클래스를 사용하는 이유는 추상화된 현실의 개념을 구체적인 파이썬 코드로 표현하기 위해서 입니다.
<br> 예를 하나 들자면 만약에 우리에게 흑백사진이 있다면 현재 21세기에서는 흑백사진을 주로 사용하지는 않고 , 
색이 있는것을 좋아하는데요
그럴때 사용하는것이 바로 Class 입니다 . Class에는 '인스턴스' 라는것이 존재하는데요 
<strong>인스턴스에는 색, 이름등등 구체적인 값을 가지고 있습니다.</strong>

파이썬에서 CLass를 정의하는방법은 밑에와 같습니다
<pre>
<code>
class Cat:
  def meow(self): #meow() 메소드 정의입니다
  print('야옹 야옹')
  
cat1 = Cat() #인스턴스 생성
cat1.meow() #메소드 호출 
</code>
</pre>

위에처럼 하시면 출력값은 결국 '야옹 야옹' 으로 출력이 되는데요. Class는 두가지로 나눌수 있습니다.

<pre>
<code>
#클래스 정의

Class ClassName:
  '''인스턴스 변수와 메소드 구현'''
  
  #인스턴스 생성과 메소드 호출
    cat1 = Cat() #Cat인스턴스 생성 cat1이 이것을 창조했습니다.
    cat1.meow() #Cat가 구현한 메소드 호출입니다.
</code>
</pre>
    
위에처럼 파이썬 Class는 두가지로 나눠서 실행을 할수가 있구요.
가끔 이럴때가 있습니다. 같은 class를 두번 사용해야하는경우 그러면 어떻게 해야할까요?
단지 그냥 Class 를 두번 생성해서 메소드 호출을 두번이나 해야할까요?
정답은 아닙니다. 그러면 어떻게 두번을 출력시킬수 있느냐?

<pre>
<code>
Class ClassName:
  '''인스턴스 변수와 메소드 구현'''
    cat1 = Cat() 
    cat1.meow()
    cat2 = Cat()
    cat2.meow()
</code>
</pre>

위에 코드처럼 하시면 됩니다. 그러면 출력값은 제가 정해둔 메소드로 출력이 두개가 되구요.

<h2> 인스턴스 변수 생성</h2>
인스턴스를 function으로 생성할때는 어떻게 해야할까요?
우선 제가 쓴 밑에 코드를 보시면 됩니다.

<pre>
<code>
Class Person:
  def info(self):
  self.name = "현준"
  self.age = 17 (int라서 따옴표 안붙입니다.)
  print('학생의 이름은' , self.name , '나이는' , self.age , '입니다.'> 
</code>
</pre>

이런식으로 사용을 하면 됩니다.

<h1>Self</h1>
<ol>
<li>파이썬의 self는 클래스의 인스턴스를 지칭합니다. self키워드를 통하여 
  클래스의 메소드와 속성에 접근할수 있습니다.</li>
  
<li> 모든 메소드의 첫 번째 매개변수는 자기 자신을 가리키는 self 변수입니다.
  즉 이 메소드는 호출한 현재 객체를 의미합니다. </li>
</ol>

한번 제가 self를 사용해서 조금 해석이 필요하지만 주석으로 설명드리겟습니다.

<pre>
<code>
class Cat:
    def __init__(self, name = "나비" , color = "흰색"): #name은 나비로 정하고 , #color은 흰색으로 정했습니다
        self.name = name #그걸 self.name과 self.color에 대입을 시켜서 그러면 self.name과 self.color은 name과 color의 역활을 하는겁니다
        self.color = color  
    def info(self): #출력시키기 위함
        print('고양이 이름은' , self.name , '색깔은' , self.color)
cat1 = Cat("네로","흰색")
cat2 = Cat("미미" , "갈색")

cat1.info()
cat2.info()
</code>
</pre>

위에 코드까지 해석을 완료했네요. class 정의와 self는 여기까지입니다.

# Python(ENG.ver)
<h4>Please note that all translations have used Google Translator</h4>

<h1>Class definition and self 2021.03.19</h1>

<h1>Class</h1><br>
The reason for using classes is simple. The reason for using classes is to express the concept of abstracted reality in concrete Python code.
<br> For example, if we have black and white photos, the current 21st century does not mainly use black and white photos,
I like the color
In that case, it is Class. There is an'instance' in the class.
<strong>Instances have specific values ​​such as color, name, etc.</strong>

Here's how to define CLass in Python:
<pre>
<code>
class Cat:
  def meow(self): #meow() method definition
  print('meow meow')
  
cat1 = Cat() #create instance
cat1.meow() # method call
</code>
</pre>

If you do as above, the output value will eventually be output as'Meow Meow'. Class can be divided into two.

<pre>
<code>
#Class definition

Class ClassName:
  '''Instance variables and method implementations'''
  
  #Instance creation and method call
    cat1 = Cat() #Cat instance creation cat1 created this.
    cat1.meow() This is a method call implemented by #Cat.
</code>
</pre>
    
As above, Python Class can be divided into two and executed.
Sometimes this is the case. What if you need to use the same class twice?
Should I just create a Class twice and call the method twice?
Not the correct answer. So how can you print twice?

<pre>
<code>
Class ClassName:
  '''Instance variables and method implementations'''
    cat1 = Cat()
    cat1.meow()
    cat2 = Cat()
    cat2.meow()
</code>
</pre>

You can do it like the code above. Then, the output value is the method that I have set, and the output is two.

<h2> Create instance variable</h2>
What to do when creating an instance as a function?
First of all, you can look at the code below that I wrote.

<pre>
<code>
Class Person:
  def info(self):
  self.name = "Hyunjun"
  self.age = 17 (Because it is an int, it is not quoted.)
  print('Student's name is', self.name,'age is', self.age,'.'>
</code>
</pre>

You can use it like this.

<h1>Self</h1>
<ol>
<li>Python's self refers to an instance of a class. through the self keyword
  You can access the methods and properties of the class.</li>
  
<li> The first parameter of any method is the variable self, which points to itself.
  In other words, this method refers to the current object called. </li>
</ol>

Once I use self, it needs some interpretation, but I'll explain it with a comment.

<pre>
<code>
class Cat:
    def __init__(self, name = "butterfly", color = "white"): #name is set to butterfly, #color is set to white
        self.name = name # By substituting it into self.name and self.color, then self.name and self.color play the role of name and color.
        self.color = color
    def info(self): #for printing
        print('The cat's name is', self.name,'the color is', self.color)
cat1 = Cat("Nero","White")
cat2 = Cat("Mimi", "Brown")

cat1.info()
cat2.info()
</code>
</pre>

You have completed the interpretation of the code above. That's all for class definition and self.

<h1>Class이해하기 2021.03.21</h1> 
<h6>눈 건강 악화로 내용은 22일에 적었음을 알립니다</h6>

클래스(class)란 무엇일까요?
우선 클래스는 '객체지향 프로그래밍 언어'에서 중요한 단어입니다. 
클래스는 개발자가 정한 이름으로 만든 독립된 공간입니다. 그것을 클래스에서는 이름공간(name space) 라고 부릅니다.

클래스에서 가장 중요한 구성요소는 클래스의 '변수'의 역활을 해주는 클래스 멤버와 같은 역활을 하는 '클래스 메소드' 입니다
클래스 멤버나 클래스 메소드는 클래스 공간 내에서 정의(define)되는것 말고는 보통의 역활은 비슷합니다.

그러면 클래스는 어떻게 define할까요?

<pre>
<code>
class 클래스 이름:
  클래스 멤버 정의
  클래스 메소드 정의
</code>
</pre>
위에처럼 클래스를 정의하시면 됩니다.

한번 Myclass 라는 이름의 클래스를 define해보겟습니다. 그러면 밑에 코드처럼 작성을 할수 있는데요.
<pre>
<code>
class MyClass:
  var = '안녕하세요'
  def sayHello(self):
    print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()

#출처 : 파이썬 200J
</code>
</pre>

# Python ENG.ver
<h1>Understanding Class 2021.03.21</h1>
<h6>We inform you that the content was written down on the 22nd due to deteriorating eye health</h6>
<h6>All translations inform you that Google Translate was used</h6>

What is a class?
First of all, class is an important word in'object-oriented programming language'.
A class is an independent space created with a name determined by the developer. It is called a namespace in a class.

The most important component of a class is a'class method' that acts like a class member that acts as a'variable' of the class.
Class members or class methods usually play similar roles, except that they are defined within the class space.

So how do you define a class?

<pre>
<code>
class class name:
  Class member definition
  Class method definition
</code>
</pre>
Just define the class as above.

Let's define a class named Myclass. Then you can write it like the code below.
<pre>
<code>
class MyClass:
  var ='Hello'
  def sayHello(self):
    print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()

#Source: Python 200J
</code>
</pre>

<h1>class 이해하기(2) 2021.03.22</h1>
클래스 멤버는 클래스 메소드 밖에서 정의되는 function입니다.

클래스 멤버는 클래스 메소드 내에서 정의되는 지역변수(함수내에서만 유효한 함수) 나 인스턴스 멤버와는 성질이 다릅니다.

클래스 메소드는 클래스 내에서 정의되는 함수입니다.
클래스 메소드는 첫번째 인자(Arguments)는 무조건 필수적으로 self입니다.
self: 클래스의 인스턴스 객체를 가르키는 참조자 입니다.

<h2>클래스를 실제 코드에서 사용하는 방법</h2>
클래스를 실제 코드에서 사용하려면 우선 인스턴스 객체로 만들어야합니다. 인스턴스 객체로 만든다는 의미는 선언적인 의미인 클래스를 실제로 사용 가능한 형태로 만든다는 뜻입니다.

<h3>클래스를 인스턴스 객체로 만드는 방법?</h3>
방법은 간단합니다. <strong>클래스를 함수 호출하듯이 하면 됩니다. 예를 들어보자면 MyClass를 인스턴스 객체로 만들기 위해선 MyClass()룰 호출하면 됩니다.</strong>

6라인에서는 MyClass의 인스턴스객체를 obj로 지정합니다.

obj의 멤버 또는 메소드를 호출하는 방법

<pre>
<code>
obj클래스 멤버 #MyClass의 클래스 멤버
obj.클래스 메소드 #MyClass의 클래스 메소드
</code>
</pre>
 
이런식으로 쓰면됩니다 obj.var는 MyClass의 클래스 멤버 var을 나타냅니다. 밑에 코드에서 var을 나타내는것은 그러면 '안녕하세요' 가 됩니다.
<pre>
<code>
class MyClass:
  var = '안녕하세요'
  def sayHello(self):
    print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()

#출처 : 파이썬 200J
</code>
</pre>

obj.sayHello()는 MyClass의 sayHello()를 호출합니다. 인스턴스객체에서 클래스메소드를 호출할 경우 첫번째 Arguments인 self는 생략 됩니다.


# Python ENG.ver
<h1>Understanding class (2) 2021.03.22</h1>
<h6>All translations inform you that Google Translator was used.</h6>
Class members are functions that are defined outside of a class method.

Class members have different properties from local variables (functions only valid within functions) or instance members defined within class methods.

Class methods are functions defined within a class.
For class methods, the first Arguments is essentially self.
self: A reference to an instance object of the class.

<h2>How to use classes in real code</h2>
To use the class in real code, you first need to make it an instance object. Making it an instance object means making a class in a form that is actually usable, which is declarative.

<h3>How to make a class an instance object?</h3>
The method is simple. You can just call the <strong> class as if it were a function call. For example, to make MyClass an instance object, you can call MyClass().</strong>

In line 6, the instance object of MyClass is designated as obj.

How to call a member or method of obj

<pre>
<code>
obj class member #MyClass class member
obj.class method #MyClass's class method
</code>
</pre>
 
You can write something like this: obj.var represents the class member var of MyClass. In the code below, var is then'Hello'.
<pre>
<code>
class MyClass:
  var ='Hello'
  def sayHello(self):
    print(self.var)

obj = MyClass()
print(obj.var)
obj.sayHello()

#Source: Python 200J
</code>
</pre>

obj.sayHello() calls sayHello() of MyClass. When calling a class method from an instance object, the first Arguments, self, are omitted.

<h1>Python Class 진짜 쉽게 이해하기 2021.03.24</h1>
어제도 그저께도 class를 공부했는데 왜 아직도 class에서 못벗어나냐면 제가 보기엔 파이썬에서는 예외처리와 class가 가장 높은벽인거 같습니다.
비록 개인차가 있겠지만 저에게는 class가 조금 많이 어렵더군요 중복커밋 죄송합니다.

<h1>class 쉽게 이해하기전 배경스토리</h1>
저는 class를 쉽게 이해하기 위해서 유튜브에서 영상을 보고 참고했는데 한가지 예를 들어서 이해를 했었습니다.
우선 저는 자소서를 예로 들겠습니다. 저는 '전'씨 니깐 전 대리가 있었다고 하겠습니다.

전 대리는 사장님께서 말씀하신 '신입 채용 공고'를 올리게 되었는데요 , 전 대리가 다니는 회사는 매우매우 작은 회사라 공고를 올렸는데 결국 3명의 지원자가 있었습니다.
<pre>
<code>
이름: 홍길동
나이: 30

이름:김철수
나이:28

이름:이영희
나이:25

</code>
</pre>
이런식으로 지원자가 와서 전 대리는 이걸 파이썬으로 저장해두고 갑니다 그러면 전 대리는 아직 파이썬 초보니깐 단지 function으로 저장해두고 가겟죠 밑에 코드처럼
<pre>
<code>
name_1 = 홍길동
age_1 = 30

name_2 = 김철수
age_2 = 28

name_3 = 이영희
age_3 = 25

</code>
</pre>

이런식으로 정리를 해두고 갑니다. 그 다음날 지나가는 선배께서 그냥 class로 정리를 하면 편하겟다고 하십니다.
class로 해두면 1,2,3 이런식으로 안해도 되서 인데요.
그래서 일단 전 대리는 class를 만들어봅니다

<pre>
<code>
class JSS():
    def __init__(self):
        self.name = input("이름")
        self.age = input("나이")
        
</code>
</pre>
이런식으로 class를 만들었는데요 여기서 전 대리는 의문점이 듭니다. 그러면 <strong>__init__</strong>이 뭐지?
init는 class를 실행하는 순간 실행이 되는 함수입니다. 한마디로 a = JSS() 라는 함수를 만들어 놓고 , a에 할당하고나서 이 코드를 실행하게 된다면
init함수의 내용이 실행되는것입니다.

이렇게 말하니깐 어려우니 쉽게 예시를 보여드리자면 
<pre>
<code>
class JSS():
    def __init__(self):
        print("안녕")
    def show(self):
        print("show 실행!")
a = JSS()
a.show()    
</code>
</pre>
이런 코드를 볼때 아마 class를 모르는 분들은 매우 어렵게 보이실텐데 저는 이 코드를 진짜 쉽게 해석해드릴께요
일단 제가 밑에 a = JSS()라고 쓴것은 init를 출력합니다 즉 "안녕"을 출력하죠 , 그러면 show()는? "당연히 show 실행!" 을 출력합니다.
a. , a = 이라고 할때 a 는 self라고 보시면 편합니다.

<h1>class 스토리 내용 활용</h1>
이제 내용은 아실테니 활용을 해보겟습니다. 저는 그후 기록을 해두려고 input함수를 사용해서 좀 더 현실적인 코드를 만들어보겟습니다.
<pre>
<code>
class JSS():
    def __init__(self):
        self.name = input("이름")
        self.age = input("나이")
    def show(self):
        print("나의 이름은 {} , 나이는 {}살입니다.".format(self.name,self.age))
a = JSS()
a.show()      
</code>
</pre>
이런 코드를 사용하게되면 출력값은 문자열 포맷팅(format)을 사용하여 input의 입력값을 받은후 출력이되는데요.
이런식으로 입력값을 받으니 그러면 출력값은 바뀝니다.

self : 클래스를 저장할 변수 
-> JSS class를 만들고 그 안에 show 라는 함수 괄호안에  self를 넣는다는것은 a라는 변수에 JSS Class를 할당했을때, a.show() 이러한 형태를
쓰겟다고 하는것이기 때문에 ()안에는 아무것도 안넣는것입니다.

self는 a. , a = 역활입니다

<h1>성별추가 (상속사용)</h1>
만약 지원자들의 나이와 이름은 아는데 , 갑자기 성별을 알아야해서 성별을 받은후에는 class를 어떻게해야 할까요?
성별은 홍길동 : 남 , 김철수 : 여 , 이영희 : 남 입니다.

이럴때는 '상속' 을 사용하면 됩니다.
<pre>
<code>
a = JSS()
a.name = "홍길동"
a.age = 30

#이랫던 코드에 상속을하면

a = JSS2()
a.name = "홍길동" 
a.age = 30
a.gender = "남"
</code>
</pre>

이런식으로 써주시면 됩니다. 그러면 활용코드는 어떻게 쓸까요?

일단 밑에 코드에 주석과 코드를 봐주세요
<pre>
<code>
class JSS2(JSS):
  def __init__(self): #여기서 init를 사용하면 기본 정보가 초기화되고 , 새로 덮어쓰게 되므로
      super().__init__(): #그 전 input을 유지함
      self.gender = input("성별") #새롭게 추가함
      
</code>
</pre>

그러면 그냥 똑같은걸 만들고 싶다면 어떻게 해야 할까요?
바로 pass 입니다 밑에 코드처럼 활용하면 됩니다.

<pre>
<code>
class JSS2(JSS):
  def __init__(self): 
      pass
a.JSS2() #init는 초기화됬으니 , 그냥 JSS가 똑같이 출력됨
</code>
</pre>

# Python ENG.ver
<h1>Python Class really easy to understand 2021.03.24</h1>
<h6>All translations inform you that Google Translator was used</h6>
I studied classes yesterday and yesterday, but the reason why I still can't get out of class is that exception handling and class are the highest walls in Python.
Although there may be individual differences, the class was a bit difficult for me. I'm sorry for duplicate commit.

<h1>Class background story before easy understanding</h1>
In order to understand the class easily, I watched the video on YouTube and referenced it, but I understood it with an example.
First of all, I will take a self-help book as an example. Since I'm'I', I'll say that I had a representative.

The former assistant manager posted the'new recruitment announcement' that the boss said, but the company he works for is a very, very small company, and in the end there were 3 applicants.
<pre>
<code>
Name: Hong Kil-dong
Age: 30

Name: Kim Chul-soo
Age: 28

Name: Lee Young-hee
Age: 25

</code>
</pre>
In this way, the applicant comes and the former deputy saves this in Python. Then, since the former deputy is still a beginner in Python, I will just save it as a function. Like the code below
<pre>
<code>
name_1 = Hong Kil-dong
age_1 = 30

name_2 = Kim Chulsoo
age_2 = 28

name_3 = Younghee Lee
age_3 = 25

</code>
</pre>

I keep it organized in this way. The next day, a passing senior said that it would be more convenient if you just organized it into a class.
If you make it as a class, it is because you don't have to do it like 1,2,3.
So, first of all, I try to create a class

<pre>
<code>
class JSS():
    def __init__(self):
        self.name = input("name")
        self.age = input("age")
        
</code>
</pre>
I created a class like this, but here I have a question. So what is <strong>__init__</strong>?
init is a function that is executed the moment the class is executed. In short, if you create a function called a = JSS(), assign it to a, then run this code
The contents of the init function are executed.

It’s difficult to say this, so let’s easily show you an example
<pre>
<code>
class JSS():
    def __init__(self):
        print("hello")
    def show(self):
        print("run show!")
a = JSS()
a.show()
</code>
</pre>
When looking at a code like this, it may seem very difficult for those who do not know the class, but I will interpret this code really easily.
Once I write a = JSS() at the bottom, it prints init, that is, it prints "hello", then show()? "Of course, run the show!" Output.
a. When we say, a =, it is convenient to see that a is self.

<h1>Use of class story content</h1>
Now I'll know the content, so I'll use it. After that, I will use the input function to make a more realistic code to record.
<pre>
<code>
class JSS():
    def __init__(self):
        self.name = input("name")
        self.age = input("age")
    def show(self):
        print("My name is {} and my age is {}.".format(self.name,self.age))
a = JSS()
a.show()
</code>
</pre>
When you use this code, the output value is output after receiving the input value of the input using string formatting.
When you receive an input value in this way, the output value changes.

self: variable to store class
-> Creating a JSS class and putting self in parentheses of a function called show in it means that when the JSS Class is assigned to a variable called a, a.show() has this form.
Because it is said to be used, nothing is put in ().

self is a. , a = role

<h1>Gender addition (inheritance use)</h1>
If I know the age and name of the applicants, but suddenly I need to know the gender, what should I do in the class after receiving the gender?
Gender is Kildong Hong: Male, Chulsoo Kim: Female, Younghee Lee: Male.

In this case, you can use'inheritance'.
<pre>
<code>
a = JSS()
a.name = "Hong Gil Dong"
a.age = 30

#If you inherit this code

a = JSS2()
a.name = "Hong Gil Dong"
a.age = 30
a.gender = "male"
</code>
</pre>

You can write it like this. Then, how do you write the utilization code?

First, look at the comments and code in the code below
<pre>
<code>
class JSS2(JSS):
  def __init__(self): #If you use init here, the default information will be initialized and overwritten.
      super().__init__(): # keep the previous input
      self.gender = input("Gender") #Newly added
      
</code>
</pre>

So what if you just want to make the same thing?
It is pass. You can use it like the code below.

<pre>
<code>
class JSS2(JSS):
  def __init__(self):
      pass
a.JSS2() #init has been initialized, so JSS is output the same
</code>
</pre>

