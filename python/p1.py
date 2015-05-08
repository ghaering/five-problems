def sum_for(lst):
    result = 0
    for number in lst:
        result += number
    return result

def sum_while(lst):
    result = 0
    idx = 0
    while idx < len(lst):
        result += lst[idx]
        idx += 1
    return result

def sum_recursive(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_recursive(lst[1:])

if __name__ == "__main__":
    lst = [3, 4, 5, 6]
    correct = sum(lst)
    assert sum_for(lst) == correct
    assert sum_while(lst) == correct
    assert sum_recursive(lst) == correct
    assert sum_recursive([]) == 0
    assert sum_recursive([5]) == 5
