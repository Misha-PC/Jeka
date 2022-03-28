

def slice_array(ar: list, part_count: int):
    part_size = ar.__len__() // part_count
    part_leftover = ar.__len__() % part_count
    result = list()
    i = 0
    for _ in range(part_count):
        i_old = i
        i += part_size
        if part_leftover:
            i += 1
            part_leftover -= 1
        result.append(ar[i_old:i])

    return result


array__ = [i for i in range(500)]

res = slice_array(array__, 30)

[print(f"{i}:\tlen:{r.__len__()}\t{r} ") for i, r in zip(range(res.__len__()), res)]
