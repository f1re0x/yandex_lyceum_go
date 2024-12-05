from itertools import permutations
word = '0123456789'
c = 0
for j in range(1,11):
    for i in permutations(word,j):
        x = ''.join(i)
        if x[0] != '0' and (x[-1] == '5' or x[-1] == '0'):
            c += 1
print(c + 1) #+1 случай когда число равно 0




def f(n):
    s = str(n)
    if len(s) == 11:
        return 1
    podr = []
    for i in range(9):
        if (int(s[-1]) + i)%2 == 0 and i > int(s[-1]):
            podr.append(int(s+str(i)))
        if (int(s[-1]) + i)%2 != 0 and i < int(s[-1]):
            podr.append(int(s + str(i)))
    return sum(f(i) for i in podr)
 
print(sum(f(i) for i in range(1,9)))




from itertools import product
 
count = 0
 
for i in product ('01a', repeat = 8 ):
    s = ''.join(i)
    if s[0] != '0' and s.count('0') == 2 and s.count('a') <5:
        count += 9**s.count('1') * 5**s.count('a')
print(count)