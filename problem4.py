from itertools import combinations

pairs = list(combinations(range(100,1000),2))
prods = []
for x,y in pairs:
    p = x * y
    prod = str(p)
    if prod == prod[::-1]:
        prods.append(p)
prods = sorted(prods,reverse=True)
print(prods[0])
    