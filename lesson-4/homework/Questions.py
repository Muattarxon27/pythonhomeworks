for son in range(1, 6):
    if son == 3:
        continue  # son 3 bo‘lganda kodni o‘tkazib yuboradi
    print(son)
for son in range(1, 6):
    if son == 3:
        break  # son 3 bo‘lganda tsikl to‘xtaydi
    print(son)
for i in range(5):  # Loops 5 times (0 to 4)
    print(i)
i = 0
while i < 5:  # Runs until i reaches 5
    print(i)
    i += 1  # Manual increment

    for outer in range(3):  # Outer loop
        for inner in range(2):  # Inner loop
           print(f"Outer: {outer}, Inner: {inner}")
for i in range(1, 6):  # Outer loop (rows)
    for j in range(1, 6):  # Inner loop (columns)
        print(f"{i * j:2}", end=" ")  # Multiply numbers and print
    print()  # Newline after each row