count = 0
for x in range(1, 12):
    for y in range(1, 12):
        if (y > x * 3 ** 0.5) or (y < (x - 8) * 3 ** 0.5) or (y > (64 - 16)**(1/2)):
            count += 1
print(count)