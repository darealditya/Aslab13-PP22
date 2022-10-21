
x = set(map(int, input("List 1 : ").split()))
y = set(map(int, input("List 2 : ").split()))
n = []
for i in x:
    if i in y:
        if i not in n:
            n.append(str(i))
print(f"Terdapat {len(n)} buah duplikat yaitu ({','.join(n)})")

# Cara Kedua
# z = list(map(str, x.intersection(y)))
# print(f"Terdapat {len(z)} buah duplikat yaitu ({','.join(z)})")