param = 50          #param 이라는 function에 50을 지정합니다.
strdata = '전역변수'  #strdata라는 function에는 '전역변수' 를 지정합니다.

def func1():
    strdata = '지역변수' #func1이라는 function에서는 strdata가 '지역변수' 라고 define합니다.
    print(strdata) #strdata를 출력합니다.

def func2(param):
    param = 1

def func3():
    global param
    param = 100

func1() #strdata를 '지역변수'라고 define한  func1은 '지역변수'가 출력됩니다
print(strdata) #strdata는 맨위에서 '전역변수' 라고 지정했으니 '전역변수'라고 출력됩니다.
print(param) #param은 위에서 50을 지정했기에 , 50이 출력됩니다.
func2(param)  #func2라는 function에 param이라는 Argument(인자)를 지정합니다.
print(param) #위에서 정한대로 50은 변함없이
func3() #func3에는 Argument를 지정하지 않았기때문에 , 그냥 func3으로 지정합니다.
print(param) #그렇게 되면 fucn3은 param에서 100으로 지정했기에 100으로 출력이 됩니다.

#func3()은 param값을 변형시키는 함수입니다.
