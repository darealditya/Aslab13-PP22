
x = list(map(int,input("Angka : ").split()))
def sort(x):
    new = []
    for i in range(len(x)):
        new.append(str(min(x)))
        x.remove(min(x))
    print(" ".join((new)))
sort(x)

