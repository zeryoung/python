#list , 대괄호, 변경 가능
#tuple , 소괄호, 변경 불가
print('------------------------------tuple--------------')
t1 = (1,2, 'a','b')
print(t1[0:])
t2 = (3,4)
print(t1+t2)
print(t1*3)
print('-------------------------dic--------------------------')
# dictionary
a = {1: '파랑구름', 2: 'a', 3: '이민준'}
print(a.keys())
print(a.values())
print(a.items()) #key, value 둘다 / tuple 형식

print(1 in a)  #키가 있는지 없는지
print(a.get(4,'없음'))#키가 없을 경우 '없음'이라고 뜨게 미입력시 none

a.clear()
print('----------------------set--------------------')
#set 특징 : 중복이 없고, 순서가 없다
s1 = set([1,2,3])
s2 = {1,2,3}
print(type(s1))
print(type(s2))

l = [1,2,2,3,3]
newList = list(set(l))
print(newList)

l2 = set("Hello")
print(l2)

s3 = set([1,2,3,4,5,6])
s4 = set([4,5,6,7,8,9])
print(s3 & s4) #& 교집합
print(s3.intersection(s4))
print(s3.union(s4))
print(s3|s4)
print(s3 -s4)
print(s3.difference(s4))
s3.add(7) #하나 추가
print(s3)
s3.update([7,8,9])
print(s3)
s3.remove(7) # 하나 제거, 리스트 불가
print(s3)

print('---------------------bool--------------------')
##불
z = [1,2,3,4]
print(type(z))
while z:
    z.pop()
    print(z)

print('-----------------------변수---------------------')
# 변수
a = [1,2,3]
b = a # b에 a가 가지고 있는 객체들의 주소를 넘겨서 주소 공유
a[1] = 4 # a를 바꾸면 b도 바뀐다.
print(a)
print(b)
## b를 바꾸면?
b[2] = 9
print(a)
print(b)
#b를 바꿔도 둘다 바뀐다 바뀌는 객체가 같기에.
print(id(a))
print(id(b))
print(a is b) # a와 b가 같은지 확인
## 두개를 다르게 하고 싶다면, 즉 객체 주소를 바꾸고 싶다면
c =[1,2,3]
d =c[:]
print(id(c))
print(id(d))
print(c is d)
c[1] =5
print(c)
print(d)

print('-------------------library----------------------')
from copy import copy
e =[1,2,3]
f =copy(e)
e[1] = 5
print(e)
print(f)
print(e is f)

g =3
h =5
g,h = h,g
print(g)
print(h)

