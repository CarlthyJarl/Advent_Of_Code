import re
import logging
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

#test2()

def test3():
    a = ["a", "b", "c"]
    for i, v in enumerate(a):
        print(i," ",v)


#test3()

def test4():
    odd_squares = {i: i*i for i in range(10)}
    print(odd_squares)
#test4()

def test5():
    logging.debug("debug info")
    logging.debug("just some info")
    logging.debug("uh ops")

def test5_main():
    level = logging.DEBUG
    fmt = '[%(levelname)s] %(asctime)s - %(message)s'
    logging.basicConfig(level=level, format=fmt)
    test5()
    
test5_main()