def count_if(lst, func):
    if not lst is list:
        raise TypeError
    if not func is function:
        raise TypeError
    return len(filter(func, lst))


def for_all_red(lst, apply, pred):
    if not lst is list:
        raise TypeError
    if not pred is function:
        raise TypeError
    if not apply is function:
        raise TypeError
    return pred(reduce(apply, lst))


def there_exists(lst, n, pred):
    if not lst is list:
        raise TypeError
    if not pred is function:
        raise TypeError
    if not n is int :
        raise TypeError
    return len(filter(pred, lst)) >= n


print for_all_red([1, 0, 8], lambda x, y: x * y, lambda x: x > 0)
print for_all_red([1, 1, 8], lambda x, y: x * y, lambda x: x > 7)
print there_exists([1, 1, 8], 1, lambda x: x > 7)
print there_exists([1, 1, 8], 2, lambda x: x > 7)
