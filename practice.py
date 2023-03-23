
counter = 0
lst = []
for num in range(0,100):
    if num%2 == 0 and num%5 == 0:
        counter +=1
        lst.append(num)

print(counter)
print(lst)
