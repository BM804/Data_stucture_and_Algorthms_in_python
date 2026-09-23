n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
hash_map = [0] * 11


for i in range(0,len(n)):
    hash_map[n[i]] += 1

print(hash_map)

for j in m:
    if j < 0 or j>10:
        print(0)
    else:
        print(hash_map[j])