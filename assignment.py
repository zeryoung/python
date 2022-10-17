#1번
h = [80,  75, 55]
total = h[0] +h[1] +h[2]
print(total/3)

10%3
#2번
a = 13
if a%2 ==0:
     print("even")
else:
    print("odd")

#3번
b = "881120-1068234"
print("19"+b[0:6]+"  "+b[6:])

#4번
pin = b
if pin[7] =="1":
    print("1"+", man")
else:
    print("2"+", woman")

#5번
c= "a:b:c:d"
c = c.replace(":","#")
print(c)

#6번
d = [1,3,5,4,2]
d.sort()
d.reverse()
print(d)

#7번
e  = ["Life", "is", "too", "short"]
f = " ".join(e)
print(f)

#8번 tuple에 항목 추가
g = (1,2,3)
print(type(g))
#tuple은 추가 불가능

#9번 오류 나는거 찾기
h = dict()
print(h)
# 다음 중 오류가 나는 것은? 4번
h['name'] = 'python' # name 키에 python value
h[('h',)] = 'python' # ('h',)가 키
#h[[1]] = 'python' # lsit의 첫번째를 지정하는 것이기 때문에 불가능
h[250] = 'python' # 250이 키
print(h)
#[] 안에 넣은게 특정 키 지목

#10번 'B'에 해당하는 값 추출
i = {'A':90, 'B':80, 'C':70}
print(i.pop('B'))
print(i)

#11번 중복 제거
j = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
k = set(j)
print(k)
l = list(k)
print(l)

#12번 이 경우 b의 값은 어떻게 될까? 그 이유는
a = b = [1, 2, 3]
a[1] = 4
print(b)
## b = [1,4,3]
### why? a와 b는 같은 주소를 공유하기 때문에 a를 바꾸면 b도 바뀐다. 
### 이렇게 하고 싶지 않을 경우 a = b가 아닌 b =a[:] 슬라이싱으로 추출한다.