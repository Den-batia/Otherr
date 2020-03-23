graf = {}
count = {}
count['s'] = 0
count['B'] = float('inf')
count['C'] = float('inf')
count['D'] = float('inf')
count['A'] = float('inf')
count['f'] = float('inf')
parent = {}
list_s = []

graf['s'] = {}

graf['s']['A'] = 350
graf['s']['B'] = 200

graf['A'] = {}
graf['A']['C'] = 100
graf['A']['D'] = 100

graf['B'] = {}
graf['B']['A'] = 100
graf['B']['D'] = 150

graf['C'] = {}
graf['C']['D'] = 200
graf['C']['f'] = 250

graf['D'] = {}
graf['D']['f'] = 100

graf['f'] = {}

def min_count(list):
    a = float('inf')
    b = None
    for i in list:
        if i in list_s:
            continue
        if list[i] < a:
            a = list[i]
            b = i
    return b

def serch():
    a = min_count(count)

    for i in graf[a]:
        if i not in list_s:
            q = graf[a][i] + count[a]
            if q < count[i]:
                count[i] = q
    list_s.append(a)

serch()
print(count)
serch()
print(count)

serch()
print(count)

serch()
print(count)

serch()
print(count)

print()

if __name__ == '__main__':
    print(1111)