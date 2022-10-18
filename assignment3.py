#Q1 주어진 자연수가 홀수인지 짝수인지 판별해 주는 함수(is_odd)를 작성해 보자.
from dataclasses import replace


def is_odd(a):
    if a%2 ==1:
        print("odd")
    else:
        print("even")

is_odd(2)
is_odd(9)

# lambda
is_odd_ = lambda x: True if x % 2 == 1 else False
is_odd_(3)


#2 입력으로 들어오는 모든 수의 평균 값을 계산해 주는 함수를 작성해 보자.
# (단 입력으로 들어오는 수의 개수는 정해져 있지 않다.)

def avg(*args):
    sum =0
    for i in args:
        sum +=i
    print(sum/len(args))
    return(sum/len(args))

avg(1,2,3,4,99)

#3 다음은 두 개의 숫자를 입력받아 더하여 돌려주는 프로그램이다.
input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")
#
#total = input1 + input2
#print("두 수의 합은 %s 입니다" % total)
#3과 6을 입력했을 때 9가 아닌 36이라는 결괏값을 돌려주었다.
# 이 프로그램의 오류를 수정해 보자.
total = int(input1) + int(input2)
print("두 수의 합은 %d 입니다" % total)

#4번 다음 중 출력 결과가 다른 것 한 개를 골라 보자.
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

#1. youneedpython / 2. youneedpython / 3. you need python / 4. youneedpython

#5번 다음은 "test.txt"라는 파일에 "Life is too short" 
# 문자열을 저장한 후 다시 그 파일을 읽어서 출력하는 프로그램이다.
# 이 프로그램은 우리가 예상한 "Life is too short"라는 문장을 출력하지 않는다. 
# 우리가 예상한 값을 출력할 수 있도록 프로그램을 수정해 보자.
f1 = open("test.txt", 'w')
f1.write("Life is too short")
f1.close() # 한번 열었으면 닫아야 다시 열지
f2 = open("test.txt", 'r')
print(f2.read())
f2.close()

#6번 사용자의 입력을 파일(test.txt)에 저장하는 프로그램을 작성해 보자.
# (단 프로그램을 다시 실행하더라도 기존에 작성한 내용을 유지하고
# 새로 입력한 내용을 추가해야 한다.)
with open("test.txt", "a") as f:
    f.write("\n life is too short, you need python")

#7번 다음과 같은 내용을 지닌 파일 test.txt가 있다.
# 이 파일의 내용 중 "java"라는 문자열을 "python"으로 바꾸어서 저장해 보자.

f3 = open("test.txt", 'w')
f3.write("Life is too short \n you need java")
f3.close() 
f4 = open("test.txt", 'r')
data = f4.read()
f4.close()
if "java" in data:
    data = data.replace("java","python")
    print(data)

with open("test.txt", "w") as g:
    g.write(data)

