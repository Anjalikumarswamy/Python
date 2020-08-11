l =[]

for x in range(0,10):
    l.append(x)

print(l)

#With comprehensions reduce the line of code.
l = [x for x in range(0,9)]
t = tuple(x for x in range(0,9))
s = {x for x in range(0,9)}
d = {x : x*x for x in range(0,9)}

print(l)
print(t)
print(s)
print(d)