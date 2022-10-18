#1번 다음 코드의 결괏값은 ?
a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")
#shirt
# wife가 없으니 X / python, you 둘다 있기에 not에 따라 X /
# need도 있지만 elif는 그렇지 않으면 이기에 우선순위에 따라 shirt

#2번 while문을 사용해 1부터 1000까지의 자연수 중 3의 배수의 합을 구해 보자.
b = 1
sum =0
while b <= 1000:
    if b%3 ==0:
        sum = sum +b #다르게 표현 sum += b
        b= b+1     #여기도
    else:           
        b = b+1    #여기도 라면 else:를 없애고 b +=1을 if와 동격으로 넣어도 됨
print(sum)

b = 1
sum =0
while b <= 1000:
    if b%3 ==0:
        sum += b 
    b= b+1    
print(sum)

#3 while문을 사용하여 다음과 같이 별(*)을 표시하는 프로그램을 작성해 보자.
# *\**\***\****\*****
c=1
while c <6:
    print("*"*c)
    c = c+1

#다른 방식
c=0
while True:
    c +=1
    if c > 5:break
    print("*"*c)
print(c , "\n")

#4 for문을 사용해 1부터 100까지의 숫자를 출력해 보자.
for d in range(1,101):
    print(d)

#5 A 학급에 총 10명의 학생이 있다. 이 학생들의 중간고사 점수는 다음과 같다.
## [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
### for문을 사용하여 A 학급의 평균 점수를 구해 보자.

e =[70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

sum = 0
for f in e:
    sum = sum+f #for문으로 list할때는 인덱스 안 잡아줘도 됨
print(sum/10)

#6 리스트 중에서 홀수에만 2를 곱하여 저장하는 다음 코드가 있다, 
# 아래를 리스트 내포로 표현해보자
numbers = [1, 2, 3, 4, 5]
#result = []
#for n in numbers:
#    if n % 2 == 1:
#        result.append(n*2)

result = [n*2 for n in numbers if n%2 ==1 ]
print(result)