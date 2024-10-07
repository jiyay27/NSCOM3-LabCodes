c = 1/2 #case factor
N = 100000 #data rate
r = 1 #ratio

S = c * N * (1/r) #signal rate

print (f"{S/1000:.4g} kBauds")