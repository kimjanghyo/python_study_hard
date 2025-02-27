

---

## 목차

1. 반복문의 정의  
2. 반복문의 종류  
3. 반복문의 예시 (코드 예제 포함)  
4. 반복문 관련 용어  
5. 반복문 사용 시 주의사항  
6. 반복문 이해에 필요한 추가 요소  
7. 결론 및 요약  
8. 추가 연습 및 실습 예제

---

## 1. 반복문의 정의

### 1.1 반복문이란?

반복문은 프로그래밍 언어에서 특정 코드 블록이나 명령어를 **여러 번 반복 실행**하도록 설계된 제어 구조입니다. 반복문을 사용하면 동일한 작업을 매번 코드를 중복해서 작성할 필요 없이, 한 번의 작성으로 반복 실행할 수 있으므로 코드의 간결성 및 유지보수성을 크게 향상시킬 수 있습니다.

### 1.2 반복문 사용의 필요성

- **코드의 재사용성 증대:** 동일한 작업을 반복해서 실행할 경우, 반복문을 사용하면 코드의 중복 작성을 방지할 수 있습니다.
- **코드의 간결함:** 반복되는 작업을 단일 구조 내에서 처리할 수 있으므로 코드의 가독성이 높아집니다.
- **유지보수의 용이성:** 반복문을 사용함으로써 수정할 사항이 발생할 때, 해당 코드 블록만 수정하면 되므로 유지보수가 용이합니다.
- **동적 데이터 처리:** 반복문의 조건에 따라 입력 데이터의 크기나 조건에 맞게 동적으로 반복 횟수를 결정할 수 있습니다.

### 1.3 반복문이 사용되는 예

- **리스트나 튜플 등의 자료형의 모든 원소를 순회하며 처리할 경우**  
- **특정 조건이 만족될 때까지 계속 실행해야 하는 알고리즘 구현 시**  
- **사용자 입력을 지속적으로 받아 처리할 경우**  
- **게임의 프레임 처리, 애니메이션 제어, 서버의 요청 처리 등**

---

## 2. 반복문의 종류

파이썬에서는 주로 두 가지 반복문을 제공합니다. 각각의 반복문은 상황에 따라 적절하게 사용될 수 있습니다.

### 2.1 for 반복문

**특징:**  
파이썬의 `for` 반복문은 리스트, 튜플, 문자열, 딕셔너리 등 **이터러블(iterable)** 객체의 각 요소를 순차적으로 접근하는 데 주로 사용됩니다.

**사용 상황:**  
- 요소의 개수가 명확하게 정해져 있을 때
- 순차적인 데이터 처리나 요소의 순회가 필요할 때

예를 들어, 리스트에 포함된 모든 항목을 출력하거나, `range()` 함수를 사용하여 일정 범위의 숫자를 반복 처리할 때 사용됩니다.

### 2.2 while 반복문

**특징:**  
`while` 반복문은 주어진 조건식이 참(`True`)인 동안 계속해서 코드 블록을 실행합니다.

**사용 상황:**  
- 반복 횟수가 사전에 명확하지 않을 때
- 특정 조건이 만족될 때까지 반복 실행할 필요가 있을 때

예를 들어, 사용자로부터 입력을 계속 받아 조건에 따라 반복을 종료하거나, 조건에 따라 반복 실행하는 알고리즘 구현 시 사용됩니다.

### 2.3 기타 반복 제어 구문

파이썬에서는 반복문을 제어하기 위한 추가 구문도 제공됩니다.

- **break:**  
  반복문 내에서 특정 조건이 만족되면 반복을 즉시 종료하는 데 사용합니다.
  
- **continue:**  
  현재 이터레이션의 나머지 코드를 건너뛰고, 다음 반복으로 진행하도록 합니다.
  
- **else:**  
  반복문이 정상적으로 종료되었을 때(즉, 중간에 `break` 문이 실행되지 않았을 때) 실행되는 블록을 지정할 수 있습니다.

또한, 리스트 내포(List Comprehension)와 제너레이터 표현식 등도 반복문을 대체하거나 보완하는 기능으로 활용될 수 있으나, 초심자에게는 기본 반복문 개념을 충분히 숙지한 후 학습하는 것이 바람직합니다.

---

## 3. 반복문의 예시 (코드 예제 포함)

본 절에서는 초심자도 쉽게 이해할 수 있도록 `for` 반복문과 `while` 반복문에 대한 다양한 코드 예제를 제공합니다. 각 예제에는 주석을 포함하여 코드의 동작 원리를 상세하게 설명하고 있습니다.

### 3.1 for 반복문 예제

#### 예제 1: 리스트의 각 요소 출력

```python
# 과일 이름이 저장된 리스트를 정의합니다.
fruits = ["사과", "바나나", "오렌지", "포도"]

# for 반복문을 사용하여 리스트의 각 요소를 순차적으로 접근합니다.
for fruit in fruits:
    # 반복 실행 시, 변수 'fruit'는 리스트의 현재 요소를 나타냅니다.
    print(fruit)  # 현재 과일의 이름을 출력합니다.
```

**설명:**  
- 리스트 `fruits`에는 여러 개의 문자열이 저장되어 있습니다.  
- `for fruit in fruits:` 문장은 리스트 내 각 요소를 순차적으로 변수 `fruit`에 할당하며 반복 실행합니다.  
- 각 이터레이션마다 `print()` 함수를 통해 해당 과일 이름을 출력합니다.

#### 예제 2: range()를 이용한 숫자 출력

```python
# range(5)는 0부터 4까지의 정수를 생성합니다.
for i in range(5):
    # 변수 'i'는 0부터 4까지 차례대로 값을 갖습니다.
    print("현재 숫자:", i)  # 현재 숫자를 출력합니다.
```

**설명:**  
- `range(5)`는 0부터 시작하여 5 미만의 정수(0, 1, 2, 3, 4)를 생성합니다.
- for 반복문은 생성된 정수를 순차적으로 변수 `i`에 대입하여 반복 실행합니다.
- 각 이터레이션마다 "현재 숫자:"와 함께 변수 `i`의 값을 출력합니다.

#### 예제 3: 문자열의 길이 출력

```python
# 문자열이 저장된 리스트를 정의합니다.
words = ["안녕하세요", "반복문", "파이썬", "코딩"]

for word in words:
    # len() 함수를 사용하여 현재 문자열 'word'의 길이를 구합니다.
    length = len(word)
    # f-string을 사용하여 문자열과 그 길이를 형식에 맞게 출력합니다.
    print(f"'{word}'의 길이는 {length}입니다.")
```

**설명:**  
- 리스트 `words`에는 여러 개의 문자열이 저장되어 있습니다.
- 각 문자열의 길이를 구하기 위해 `len()` 함수를 사용하였으며, 이를 변수 `length`에 저장합니다.
- f-string을 활용하여 문자열과 해당 길이를 포맷팅하여 출력합니다.

### 3.2 while 반복문 예제

#### 예제 1: 조건에 따른 숫자 출력

```python
# 변수 'i'를 0으로 초기화합니다.
i = 0

# 조건 i < 5가 참인 동안 반복문을 실행합니다.
while i < 5:
    print("현재 숫자:", i)  # 현재 i의 값을 출력합니다.
    i += 1  # i의 값을 1씩 증가시켜 종료 조건에 도달하도록 합니다.
```

**설명:**  
- 변수 `i`를 0으로 초기화한 후, `while i < 5:` 조건이 참인 동안 반복문을 실행합니다.
- 각 반복마다 `print()` 함수를 통해 현재 값을 출력하고, `i += 1`을 통해 변수 `i`의 값을 증가시킵니다.
- 이 과정은 `i`가 5 이상이 될 때까지 반복됩니다.

#### 예제 2: 사용자 입력에 따른 반복 종료

```python
# 사용자 입력을 저장할 변수를 빈 문자열로 초기화합니다.
user_input = ""

# 사용자가 'q'를 입력할 때까지 반복문을 실행합니다.
while user_input != "q":
    # 사용자로부터 입력을 받습니다.
    user_input = input("종료하려면 'q'를 입력하십시오: ")
    print("입력한 값:", user_input)  # 입력받은 값을 출력합니다.
```

**설명:**  
- 변수 `user_input`을 빈 문자열로 초기화한 후, 사용자가 'q'를 입력할 때까지 `while` 반복문이 실행됩니다.
- `input()` 함수를 통해 사용자의 입력을 받고, 입력된 값을 출력합니다.
- 사용자가 'q'를 입력하면 조건문이 거짓이 되어 반복문이 종료됩니다.

#### 예제 3: break와 continue의 활용

```python
# 0부터 9까지의 숫자에 대해 반복문을 실행합니다.
for num in range(10):
    # num이 5인 경우, 반복문을 즉시 종료합니다.
    if num == 5:
        print("num이 5이므로 반복문을 종료합니다.")
        break  # 반복문을 종료합니다.
    
    # num이 3인 경우, 현재 이터레이션을 건너뛰고 다음 반복으로 진행합니다.
    if num == 3:
        print("num이 3이므로 이번 이터레이션을 건너뜁니다.")
        continue  # 현재 반복의 남은 코드를 건너뜁니다.
    
    # 위 조건에 해당하지 않을 경우, 현재 num 값을 출력합니다.
    print("현재 num:", num)
```

**설명:**  
- 반복문 내에서 `if` 조건문을 사용하여 특정 상황에 대해 `break`와 `continue`를 활용하고 있습니다.
- `num == 5`인 경우 `break`를 통해 전체 반복문이 종료되며, `num == 3`인 경우 `continue`를 통해 해당 이터레이션의 나머지 코드는 실행되지 않고 다음 이터레이션으로 넘어갑니다.

### 3.3 중첩 반복문 (Nested Loops) 예제

```python
# 2차원 리스트(리스트 안에 리스트가 포함된 구조)를 정의합니다.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# 바깥쪽 for문은 각 행(row)을 순회합니다.
for row in matrix:
    # 안쪽 for문은 각 행의 요소(element)를 순회합니다.
    for element in row:
        print(element, end=" ")  # 한 행의 요소들을 같은 줄에 출력합니다.
    print()  # 한 행이 끝난 후 줄바꿈을 수행합니다.
```

**설명:**  
- 2차원 리스트 `matrix`는 각 행마다 여러 요소를 포함하는 구조입니다.
- 바깥쪽 `for` 반복문은 각 행을 순차적으로 접근하며, 내부의 `for` 반복문은 해당 행의 각 요소를 순회합니다.
- `print(element, end=" ")`를 사용하여 한 줄에 출력하고, 각 행이 끝날 때마다 `print()`를 호출하여 줄바꿈을 수행합니다.

---

## 4. 반복문 관련 용어

반복문을 이해하기 위해서는 아래와 같은 용어들을 숙지하는 것이 중요합니다.

### 4.1 이터레이션(Iteration)

- **정의:**  
  반복문에서 코드 블록이 한 번 실행되는 과정을 이터레이션이라고 합니다.
- **예시:**  
  `for i in range(5):` 구문에서는 총 5회의 이터레이션이 발생합니다.

### 4.2 루프 변수(Loop Variable) 또는 인덱스(Index)

- **정의:**  
  반복문 내에서 현재 이터레이션의 값을 저장하기 위해 사용되는 변수를 의미합니다.
- **예시:**  
  위의 예제에서는 `i`, `fruit` 등이 루프 변수의 역할을 합니다.

### 4.3 이터러블(Iterable)

- **정의:**  
  반복문을 통해 순회할 수 있는 객체를 이터러블이라고 합니다.
- **예시:**  
  리스트, 튜플, 문자열, 딕셔너리, 집합 등이 이에 해당합니다.

### 4.4 반복 제어문

- **break:**  
  특정 조건 하에서 반복문을 즉시 종료시키는 역할을 합니다.
- **continue:**  
  현재 이터레이션의 나머지 코드를 건너뛰고 다음 이터레이션으로 넘어가도록 합니다.

### 4.5 무한 반복(Infinite Loop)

- **정의:**  
  종료 조건의 부적절한 설정 등으로 인해 반복문이 영원히 종료되지 않고 계속 실행되는 상황을 말합니다.
- **예시:**  
  `while True:`를 사용한 경우, 내부에 종료 조건이 없다면 무한 반복이 발생할 수 있습니다.

### 4.6 중첩 반복문(Nested Loop)

- **정의:**  
  하나의 반복문 내에 다른 반복문이 포함된 구조를 의미합니다.
- **예시:**  
  2차원 리스트를 순회할 때 바깥쪽 반복문과 내부 반복문을 사용하는 경우가 해당됩니다.

### 4.7 루프 카운터(Loop Counter)

- **정의:**  
  반복문의 실행 횟수를 세기 위해 사용되는 변수로, 주로 반복문의 조건식에 활용됩니다.
- **예시:**  
  `while` 문에서 `i` 또는 `count` 변수 등을 사용하여 반복 횟수를 관리할 수 있습니다.

---

## 5. 반복문 사용 시 주의사항

반복문은 매우 유용한 도구이나, 부적절하게 사용될 경우 다양한 문제가 발생할 수 있습니다. 다음은 반복문 사용 시 주의해야 할 주요 사항들입니다.

### 5.1 무한 루프의 발생 방지

- **원인:**  
  반복문 내부에서 종료 조건을 올바르게 갱신하지 않거나, 조건 설정에 오류가 있을 경우 무한 루프가 발생할 수 있습니다.
- **예시:**  
  ```python
  i = 0
  while i < 5:
      print(i)
      # i의 값이 갱신되지 않으면 i < 5 조건이 영원히 참이 되어 무한 루프에 빠집니다.
  ```
- **해결책:**  
  반복문 내부에서 조건이 반드시 만족할 수 있도록 변수의 값을 적절히 갱신해야 합니다.

### 5.2 오프 바이 원(Off-by-One) 에러

- **정의:**  
  반복 횟수를 계산할 때 경계값을 잘못 설정하여 실제 필요한 반복 횟수보다 1회 적거나 많은 실행이 발생하는 오류입니다.
- **예시:**  
  `range(5)`는 0부터 4까지 생성하므로, 5까지 포함하고자 할 경우 `range(6)`를 사용해야 합니다.
- **주의사항:**  
  반복문의 시작과 종료 조건을 명확히 인지하여 올바른 조건을 설정해야 합니다.

### 5.3 변수 명명 및 들여쓰기

- **변수 명명:**  
  루프 변수나 카운터 변수는 해당 변수의 역할을 명확히 알 수 있도록 의미 있는 이름을 부여하는 것이 좋습니다.
- **들여쓰기:**  
  파이썬은 들여쓰기를 통해 코드 블록을 구분하므로, 반복문 내외의 코드 구조가 올바르게 들여쓰기 되어야 합니다.
- **결과:**  
  올바른 명명 및 들여쓰기는 코드의 가독성과 유지보수를 향상시킵니다.

### 5.4 반복문 내부의 복잡한 로직

- **설명:**  
  반복문 내부에 복잡한 조건문이나 연산이 포함될 경우 디버깅이 어려워질 수 있으므로, 필요한 경우 별도의 함수로 분리하는 것이 좋습니다.
- **예시:**  
  복잡한 데이터 처리 로직은 반복문 내부에 모두 포함하기보다는, 기능별로 분리하여 호출하는 구조를 권장합니다.

### 5.5 성능 고려

- **설명:**  
  많은 이터레이션을 수행하는 반복문은 실행 시간이 길어질 수 있으므로, 불필요한 중첩 반복이나 복잡한 연산을 피하도록 주의해야 합니다.
- **해결책:**  
  가능하다면 파이썬의 내장 함수(예: `map()`, `filter()` 등)나 벡터화 연산(numpy, pandas 등)을 활용하여 성능을 최적화할 수 있습니다.

---

## 6. 반복문 이해에 필요한 추가 요소

반복문을 단순히 문법적으로 이해하는 것뿐만 아니라, 실제 문제 해결에 어떻게 응용할 수 있는지에 대한 심도 있는 이해가 필요합니다. 다음은 반복문을 보다 효과적으로 활용하기 위해 숙지해야 할 추가 개념들입니다.

### 6.1 알고리즘과 문제 해결

- **반복문과 알고리즘:**  
  반복문은 다양한 알고리즘 구현의 핵심 구성 요소입니다.  
  예를 들어, 정렬, 탐색, 누적 합계 계산 등의 알고리즘은 반복문을 통해 효율적으로 구현할 수 있습니다.
  
- **문제 해결 전략:**  
  반복문을 사용하여 문제를 작은 단위로 분해하고, 각 단위를 체계적으로 처리하는 연습이 필요합니다.

### 6.2 디버깅 및 테스트

- **디버깅 방법:**  
  반복문이 예상대로 동작하지 않을 경우, 중간 변수 값을 출력하거나 디버거를 활용하여 각 이터레이션의 상태를 확인하는 것이 좋습니다.
  
- **테스트 케이스 작성:**  
  다양한 입력 값과 경계 조건을 고려하여 반복문이 올바르게 실행되는지 테스트하는 습관이 중요합니다.

### 6.3 리스트 내포(List Comprehension)

- **정의:**  
  리스트 내포는 기존의 for 반복문을 보다 간결하게 작성할 수 있도록 지원하는 파이썬의 문법입니다.
  
- **예시:**  
  ```python
  # 0부터 9까지의 정수 중 짝수만 포함하는 리스트 생성
  even_numbers = [num for num in range(10) if num % 2 == 0]
  print(even_numbers)  # 출력 결과: [0, 2, 4, 6, 8]
  ```
  
- **설명:**  
  리스트 내포는 조건문과 반복문을 한 줄에 작성할 수 있으며, 코드의 간결함과 가독성을 높이는 데 유용합니다.

### 6.4 제너레이터(Generators)

- **정의:**  
  제너레이터는 필요할 때마다 값을 생성하는 이터러블 객체를 생성하는 함수 또는 구문입니다.  
  이를 통해 메모리 효율적인 방식으로 반복 작업을 수행할 수 있습니다.
  
- **예시:**  
  ```python
  # 제너레이터 함수를 사용하여 1부터 n까지의 정수를 생성하는 예제
  def count_up_to(n):
      i = 1
      while i <= n:
          yield i  # 현재 i의 값을 반환하고, 함수 상태를 유지합니다.
          i += 1
  
  for number in count_up_to(5):
      print(number)  # 1부터 5까지의 정수를 순차적으로 출력합니다.
  ```
  
- **설명:**  
  제너레이터는 한 번에 모든 값을 메모리에 저장하지 않고 필요할 때마다 하나씩 생성하므로, 대용량 데이터 처리 시 유용합니다.

### 6.5 재귀(Recursion)와 반복문의 관계

- **비교:**  
  재귀와 반복문은 모두 반복적인 작업을 처리할 수 있는 방법입니다.  
  재귀는 함수가 자기 자신을 호출하면서 문제를 분할하여 해결하는 반면, 반복문은 명시적으로 이터레이션을 수행합니다.
  
- **예시 (팩토리얼 계산):**

  **반복문을 이용한 방식:**
  ```python
  def factorial_iterative(n):
      result = 1
      # 1부터 n까지 순차적으로 곱하여 결과를 도출합니다.
      for i in range(1, n + 1):
          result *= i
      return result
  
  print(factorial_iterative(5))  # 출력: 120
  ```
  
  **재귀를 이용한 방식:**
  ```python
  def factorial_recursive(n):
      # n이 1 이하일 경우 1을 반환합니다.
      if n <= 1:
          return 1
      # 재귀 호출을 통해 n * (n-1)!을 계산합니다.
      return n * factorial_recursive(n - 1)
  
  print(factorial_recursive(5))  # 출력: 120
  ```
  
- **주의사항:**  
  재귀를 사용할 경우 반드시 종료 조건(기저 사례, base case)을 명시해야 하며, 그렇지 않으면 무한 재귀에 빠질 수 있습니다.

### 6.6 효율적인 코드 작성 연습

- **연습:**  
  반복문을 활용한 다양한 알고리즘 문제(예: 피보나치 수열, 최대값/최소값 찾기, 정렬 알고리즘 등)를 직접 구현해보며 효율적인 코드 작성법을 익힙니다.
  
- **참고:**  
  다양한 온라인 코딩 플랫폼(예: 백준, 프로그래머스, LeetCode 등)에서 제공하는 문제를 풀어보며 반복문과 관련한 실전 감각을 기르는 것이 좋습니다.

### 6.7 시간 복잡도 및 메모리 고려

- **시간 복잡도:**  
  반복문의 실행 횟수에 따라 알고리즘의 시간 복잡도가 결정됩니다. 예를 들어, 리스트의 모든 요소를 한 번씩 순회하는 경우 O(n)의 시간 복잡도를 가지게 됩니다.
  
- **메모리 사용:**  
  반복문 자체는 큰 메모리를 요구하지 않으나, 반복문 내부에서 생성되는 임시 변수나 자료구조가 메모리 사용에 영향을 줄 수 있습니다.
  
- **최적화:**  
  불필요한 반복을 줄이고, 반복문 내 연산을 간소화하는 등의 방법으로 코드의 효율성을 개선할 필요가 있습니다.

---

## 7. 결론 및 요약

본 문서에서는 파이썬의 반복문에 대해 초심자도 이해할 수 있도록 다음과 같이 체계적으로 설명하였습니다.

1. **반복문의 정의:**  
   - 반복문은 특정 작업을 여러 번 실행할 수 있도록 설계된 제어 구조입니다.
   - 이를 통해 코드의 재사용성, 간결성, 유지보수성이 크게 향상됩니다.

2. **반복문의 종류:**  
   - **for 반복문:** 이터러블 객체(리스트, 튜플, 문자열 등)의 각 요소를 순차적으로 처리하는 데 사용됩니다.
   - **while 반복문:** 주어진 조건식이 참인 동안 계속해서 실행하는 구조로, 반복 횟수가 미리 정해지지 않은 경우 유용합니다.
   - 또한, `break`, `continue` 등의 반복 제어문이 존재하여 보다 세밀한 제어가 가능합니다.

3. **반복문의 예시:**  
   - 다양한 코드 예제를 통해 `for`와 `while` 반복문의 기본 사용법 및 중첩 반복문, 제어문 사용법을 설명하였습니다.
   - 각 예제에는 주석을 포함하여 초심자도 이해하기 쉽게 설명하였습니다.

4. **반복문 관련 용어:**  
   - 이터레이션, 루프 변수, 이터러블, 반복 제어문, 무한 반복, 중첩 반복문, 루프 카운터 등 필수 용어들을 정의하고 설명하였습니다.

5. **반복문 사용 시 주의사항:**  
   - 무한 루프, 오프 바이 원 에러, 변수 명명 및 들여쓰기, 반복문 내부 로직의 복잡성, 성능 이슈 등 반복문 사용 시 발생할 수 있는 문제점과 해결 방법을 다루었습니다.

6. **추가적인 학습 요소:**  
   - 리스트 내포, 제너레이터, 재귀, 시간 복잡도, 메모리 최적화 등 반복문과 관련된 고급 개념들을 소개하여, 보다 효율적인 코드 작성 및 문제 해결 능력을 배양할 수 있도록 하였습니다.

본 문서의 내용을 충분히 숙지하고 다양한 예제를 직접 실습함으로써, 초심자 분들이 파이썬의 반복문을 명확하게 이해하고 실무에 응용할 수 있기를 기대합니다.

---

## 8. 추가 연습 및 실습 예제

반복문을 이해하고 활용하는 데 도움이 되는 추가 예제들을 아래에 제시합니다.

### 예제 1: 구구단 출력

```python
# 구구단을 출력하는 프로그램입니다.
# 외부 반복문은 2단부터 9단까지 처리합니다.
for dan in range(2, 10):  # 2부터 9까지 반복
    print(f"--- {dan}단 ---")  # 각 단의 제목 출력
    # 내부 반복문은 1부터 9까지 곱셈 결과를 출력합니다.
    for num in range(1, 10):  # 1부터 9까지 반복
        result = dan * num  # 곱셈 결과 계산
        print(f"{dan} x {num} = {result}")  # 결과 출력
    print()  # 각 단 사이에 줄바꿈
```

**설명:**  
- 외부 반복문은 구구단의 각 단(2단부터 9단)을 처리하며, 내부 반복문은 각 단의 곱셈 결과(1부터 9까지)를 출력합니다.
- 중첩 반복문을 통해 2차원 형태의 데이터를 출력하는 예제를 제공합니다.

### 예제 2: 리스트에서 짝수만 선택하기

```python
# 주어진 숫자 리스트에서 짝수만을 선택하여 새로운 리스트에 저장하는 예제입니다.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []  # 짝수를 저장할 빈 리스트

# for 반복문을 통해 리스트의 각 요소를 검사합니다.
for number in numbers:
    if number % 2 == 0:  # 숫자가 2로 나누어 떨어지면 짝수입니다.
        even_numbers.append(number)  # 짝수인 경우, 리스트에 추가

print("짝수 리스트:", even_numbers)  # 결과 출력
```

**설명:**  
- 본 예제는 조건문과 반복문의 결합을 통해 리스트 내 특정 조건(짝수)을 만족하는 요소만 선택하는 과정을 보여줍니다.

### 예제 3: 사용자 입력을 통한 숫자 합계 계산

```python
# 사용자가 '끝'이라고 입력할 때까지 숫자를 입력받아, 총합을 계산하는 예제입니다.
total = 0  # 누적 합계를 저장할 변수 초기화

while True:  # 무한 반복을 시작합니다.
    user_input = input("숫자를 입력하십시오 (종료하려면 '끝'을 입력): ")
    
    if user_input == "끝":  # 사용자가 '끝'을 입력하면 반복문 종료
        break
    
    if user_input.isdigit():  # 입력값이 숫자인지 확인합니다.
        total += int(user_input)  # 숫자이면 정수형으로 변환 후 총합에 더합니다.
    else:
        print("유효한 숫자가 아닙니다. 다시 입력하십시오.")

print("입력한 숫자의 총합은:", total)
```

**설명:**  
- 사용자가 '끝'이라는 문자열을 입력할 때까지 계속해서 숫자를 입력받고, 이를 누적하여 합계를 계산하는 예제입니다.
- `while` 반복문과 조건문, 그리고 `break` 문을 활용하여 반복을 제어하는 방법을 설명합니다.

---

## 결론

본 자료에서는 파이썬 반복문의 개념을 초심자도 쉽게 이해할 수 있도록 공식적인 어조로 체계적으로 정리하였습니다.  
주요 내용은 다음과 같습니다.

- **반복문의 정의 및 필요성:**  
  반복문은 동일한 작업을 여러 번 효율적으로 수행할 수 있도록 돕는 제어 구조입니다. 이를 통해 코드의 간결성과 유지보수성을 확보할 수 있습니다.

- **반복문의 종류:**  
  파이썬에서는 `for` 반복문과 `while` 반복문을 주로 사용하며, 각각의 특징과 사용 상황에 따라 적절히 선택하여 사용합니다.

- **코드 예제:**  
  다양한 실습 예제를 통해 반복문의 기본 문법과 중첩 반복문, 조건문 및 제어문(`break`, `continue`)의 활용 방법을 살펴보았습니다.

- **반복문 관련 용어 및 주의사항:**  
  이터레이션, 루프 변수, 이터러블 등 기본 용어와 함께 무한 루프, 오프 바이 원 에러, 변수 명명, 들여쓰기 및 성능 문제와 같은 주의사항을 다루었습니다.

- **추가 학습 요소:**  
  리스트 내포, 제너레이터, 재귀, 시간 복잡도 및 메모리 최적화와 같은 고급 개념을 소개하여, 반복문을 보다 효과적으로 활용할 수 있는 방법을 제시하였습니다.

본 자료의 내용을 충분히 숙지하시고 다양한 실습 예제를 직접 작성해 보시길 권장드립니다. 반복문은 프로그래밍의 기초이자 필수적인 개념으로, 이를 탄탄히 이해하는 것이 이후 복잡한 알고리즘 문제 해결 및 실무 개발에 큰 도움이 될 것입니다.

```commandline
# for - loop 관련 수업
chosen_word = "apple"

for letter in chosen_word:
    print(letter)
    
# 결과값 :
#a
#p
#p
#l
#e
```