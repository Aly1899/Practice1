word = 'qwerewq'
if list(word) == list(word)[::-1]:
    a = True
else:
    a = False
print(a)

a = [1,2,7,4,5]
i=0
max_prod = 0
while i < len(a)-1:
    prod = a[i]*a[i+1]
    if prod > max_prod:
        max_prod = prod
    i += 1
print(max_prod)