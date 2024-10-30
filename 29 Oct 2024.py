import numpy as np
import pandas as pd

def variable_and_datatypes():
    """Variable assignment and data types"""
    # 변수에 다양한 데이터 타입을 할당
    number = 10           # 정수형 변수
    text = "Hello, AI"    # 문자열 변수
    decimal = 3.14        # 실수형 변수
    is_true = True        # 논리형 변수
    print(number, text, decimal, is_true)

def list_and_loop():
    """List and for loop example"""
    # 리스트 생성 및 for 반복문을 이용한 데이터 순회
    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        # 리스트의 각 요소에 2를 곱하여 출력
        print(number * 2)

def add_numbers(a, b):
    """Function to add two numbers"""
    # 두 수를 더한 값을 반환
    return a + b

def check_even_or_odd(number):
    """Conditional statement to check even or odd"""
    # 주어진 숫자가 짝수인지 홀수인지 확인
    if number % 2 == 0:
        print("Even")    # 짝수일 경우
    else:
        print("Odd")     # 홀수일 경우

class Dog:
    """Class representing a Dog with name and age attributes"""
    def __init__(self, name, age):
        # 강아지의 이름과 나이를 초기화
        self.name = name
        self.age = age

    def bark(self):
        """Method for Dog to bark"""
        # 강아지가 짖는 동작을 출력
        print(f"{self.name} says Woof!")

def numpy_example():
    """Example of basic operations with numpy"""
    # numpy 배열 생성 및 기본 연산 수행
    array = np.array([1, 2, 3, 4, 5])
    print("Mean:", np.mean(array))  # 배열의 평균 계산
    print("Sum:", np.sum(array))    # 배열의 합 계산

def pandas_example():
    """Example of creating and displaying a DataFrame with pandas"""
    # pandas DataFrame 생성
    data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [24, 27, 22]}
    df = pd.DataFrame(data)
    print(df)   # DataFrame 출력

if __name__ == "__main__":
    # 메인 블록에서 각 함수 호출
    
    # 변수와 데이터 타입 예제 실행
    variable_and_datatypes()
    
    # 리스트와 반복문 예제 실행
    list_and_loop()
    
    # 함수로 두 수 더하기 예제 실행
    result = add_numbers(5, 7)
    print("Addition Result:", result)
    
    # 짝수와 홀수 확인 예제 실행
    check_even_or_odd(10)
    
    # Dog 클래스 사용 예제 실행
    dog = Dog("Buddy", 3)
    dog.bark()
    
    # numpy 사용 예제 실행
    numpy_example()
    
    # pandas 사용 예제 실행
    pandas_example()
