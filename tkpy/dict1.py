def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

class Time:
    """represents the time of day ."""

def print_time(time):
    print('%.2d:%.2d:%.2d' % (time.hour, time.minute, time.second))


if __name__ == '__main__':
    print( his( 'brontosaurus' ) )
    start=Time()

