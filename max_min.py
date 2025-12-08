tab = [3, 1, 7, 2, 9]

mn = tab[0]
mx = tab[0]

for x in tab:
    if x < mn:
        mn = x
    if x > mx:
        mx = x

print("Min :", mn)
print("Max :", mx)
