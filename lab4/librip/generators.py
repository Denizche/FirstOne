import random


def field(items, *args):
    assert len(args) > 0
    for item in items:
        if len(args) == 1:
            if item.get(args[0]) is None:
                continue
            yield item[args[0]]
        else:
            dictionary = {}
            for name in args:
                if item.get(name) is None:
                    continue
                dictionary[name] = item.get(name)
            if dictionary:
                yield dictionary


def random_generator(begin, end, num_count):
    for i in range(num_count):
        yield random.randint(begin, end)


def infinite():
    i=0
    while 1:
        i = random.randint(1, 1000)
        yield i