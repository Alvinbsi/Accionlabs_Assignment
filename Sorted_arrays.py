def sorted_arrays(x):
    if not (0 <= x <= 9):
        return int(f"{x}" * 1) + int(f"{x}" * 2) + int(f"{x}" * 3) + int(f"{x}" * 4)
print(sorted_arrays([1,2,3,4], [3,4,5,6]))
