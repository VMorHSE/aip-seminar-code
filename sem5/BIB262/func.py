def func(d):
    lenghts = [len(v) for v in d.values()]
    squares = [v**2 for v in d.keys()]
    return lenghts, squares