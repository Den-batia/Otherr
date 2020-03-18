import datetime
from random import randint
def sort(arri):
    if len(arri) < 2:
        return arri
    else:
        a = arri.pop(int(len(arri)/2))
        min = [i for i in arri if i <= a]
        max = [i for i in arri if i > a]
        return sort(min) + [a] + sort(max)

s = [randint(0,i) for i in range(500000)]
print(len(s))
t1 = datetime.datetime.now()
s= sort(s)
t2= datetime.datetime.now() - t1
print('{} секунд, {} милиекунд'.format(t2.seconds, t2.microseconds/1000))
