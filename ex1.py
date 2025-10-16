row = int(input("Enter row:"))
col = int(input("Enter column:"))
srch = int(input("Search:"))

for x in range (1, row + 1):
    for y in range(1, col +1):
        ans = x *y
        if ans == srch:
            print(f"[{ans}]", end=" ")
        else:
            print(ans, end = " ")
    print()