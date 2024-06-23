res = [x*y*(1000-x-y) for x in range(1,1000) for y in range(1,1000-x) if x**2 + y**2 == (1000-x-y)**2]

print(res) #31875000