
def length_number(n):
    return len(str(n))

count = 0
for i in range(1,1000):
    for j in range(1,100):
        if length_number(i**j)==j:
            count +=1

print count
