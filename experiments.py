import go
from checkergame import partitions2checkers 

def fancy_filter(xs):
    return [x+1 for x in xs if x != 99]

f=go.test_all_problems_G(3,8)
fs = filter(lambda x: acceptable_parts(x[0]),f)
ys = map(lambda x: [map(fancy_filter,x[0]),x[1].solutions],fs)

def acceptable(lst):
    return lst[0] != 0 and lst[-1] != 99

def acceptable_parts(parts):
    return all(map(acceptable,parts))

xs = filter(lambda x: acceptable_parts(x[0]),fs)

for f in xs:
    print(f)

a = {}

for i in map(lambda x:x[1],fs):
    if i in a: 
        a[i] += 1
    else:
        a[i] = 1

#Extra data for 8
data=[[[[99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 2, 3, 99, 99, 6, 7], [99, 1, 99, 3, 99, 99, 6, 7], [99, 1, 99, 3, 99, 99, 6, 7]], 8], [[[99, 99, 2, 99, 4, 99, 6, 7], [99, 99, 2, 99, 4, 99, 6, 7], [99, 1, 99, 99, 99, 5, 6, 7], [99, 1, 99, 99, 99, 5, 6, 7], [99, 99, 2, 3, 99, 99, 6, 7]], 8]]

#Extra data for 80
[[[[99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 99, 99, 3, 99, 5, 6, 7], [99, 1, 99, 3, 99, 99, 6, 7], [99, 1, 99, 3, 99, 99, 6, 7]], 80]]

