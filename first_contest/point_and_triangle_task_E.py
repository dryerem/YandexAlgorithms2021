from math import sqrt

def is_place_on_triangle(d: int, x: int, y: int):
    if ((x + y) <= d) and x >= 0 and y >= 0:
        return 0

    # Расстояние до вершины а
    cat_one: int = abs(x)
    cat_two: int = abs(y)
    sa: float = sqrt(cat_one ** 2 + cat_two ** 2)
    
    # Расстояние до вершины b 
    cat_one: int = abs(x) - d
    cat_two: int = abs(y)
    sb: float = sqrt(cat_one ** 2 + cat_two ** 2)

    # Расстояние до вершины c
    cat_one: int = abs(x)
    cat_two: int = abs(y) - d
    sc: float = sqrt(cat_one ** 2 + cat_two ** 2)
    if ((sa < sb) and (sa < sc)):
        return 1
    elif ((sb < sa) and (sb < sc)):
        return 2
    else:
        if sa == sb or sa == sc:
            return 1
        elif sb == sc:
            return 2
        else:
            return 3

d = int(input())
x, y = map(int, input().split())
print(is_place_on_triangle(d, x, y))