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
