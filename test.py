import re
def test1():
    s = "i like me 95"
    l = [0, 11]

    if "like" in s:
        print("ya")
        l.append(int((re.findall(r'\d+',s)[0])))
        print(l)

#test1()

def test2():
    l = [25, 11, 95, 10, 25, 12]
    l2= []

    l2.append(l[0]+l[1]+l[1+1])
    print(l2)

test2()