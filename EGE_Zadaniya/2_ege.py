print("x y z w f1 f2")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                f1 = (x or y)
                f2 = (y and x)
                print(x, y, z, w, "", int(f1), "", int(f2))