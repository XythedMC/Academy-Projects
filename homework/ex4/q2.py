def merge_emps(workers1: list[list[int]], workers2: list[list[int]]) -> list[list[int]]:
    res = []
    max_list = max(workers1, workers2)
    min_list = min(workers1, workers2)

    for i in range(len(min_list)):
        res.append(min_list[i])

    