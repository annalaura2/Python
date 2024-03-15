c1 = {1, 2, 3, 4}
c2 = {5,6, 7, 8}
c3 = {7,8,9}

print(c1.isdisjoint(c2))
print(c2.isdisjoint(c1))
print(c1.isdisjoint(c3))
print(c2.isdisjoint(c3))