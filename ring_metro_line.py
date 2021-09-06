def min_count_intermediate_stations(n: int, i: int, j: int) -> int:
    count_of_stations: list = list(range(1, n + 1))
    left = []
    right = []
    if i > j:
        left = count_of_stations[j:i - 1]
        right = count_of_stations[:j - 1] + count_of_stations[i:n]
    else:
        left = count_of_stations[i:j - 1]
        right = count_of_stations[j:] + count_of_stations[:i - 1]

    return min(len(left), len(right))

m, i, j = map(int, input().split())
print(min_count_intermediate_stations(m, i, j))
