def solution(path):
    with open(path) as f:
        arr = [list(row.strip()) for row in f.readlines()]

    n_rows = len(arr)
    n_cols = len(arr[0])

    count = 0
    for i in range(1, n_rows - 1):
        for j in range(1, n_cols - 1):
            # Check all As for X-MAS:
            if arr[i][j] == "A" and (
                set((arr[i - 1][j - 1], arr[i + 1][j + 1]))
                == set((arr[i - 1][j + 1], arr[i + 1][j - 1]))
                == {"M", "S"}
            ):
                count += 1
    return count
