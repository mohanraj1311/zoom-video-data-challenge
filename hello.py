def uniquecombo(items, r):
    pool = tuple(items)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range((r))):
            if indices[i] != i + n -r:
                break
        else:
            return
        indices[i] +=1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)





def call_uniquecombo(items, n):
    res = []
    for each in uniquecombo(items, n):
        res.append(each)
    return res


def generate(n):
    items = range(1, n + 1)
    return call_uniquecombo(items, n)

def main():
    print generate(4)

if __name__=='__main__':
    main()