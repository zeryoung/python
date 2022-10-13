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