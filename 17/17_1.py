f = open('17.txt')
a = []
for i in range(5000):
    s1 = int(f.readline())
    a.append(s1)

print(a)
print(sum(a))
print(max(a))