def parni(x):
    for i in range(x):
        if i%2 ==0:
            yield i
def neparni(x):
    for i in range(x):
        if i%2==1:
            yield i

unos = int(input("Unos:")
parnih = parni(unos)
neparnih = neparni(unos)


br = zip(parnih, neparnih)
print("Parni: Neparni:")
for parni , neparni in brojevi:
           print(parni, neparni)
