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

# Python(ENGver) Please inform that all translations have been made through Google Translator.
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
