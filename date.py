x, y, z = map(int, input().split())

if (1 <= x <= 31) and (1 <= y <= 31) and (1970 <= z <= 2069):
    if x > 12 or y > 12 or x == y:
        print(1)
    else:
        print(0)