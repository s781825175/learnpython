import bisect
l=range(1000)
x=24
x_insert_point = bisect.bisect_left(l,x)
print(x_insert_point)
