from aocd import get_data
from aocd.transforms import lines
from functools import reduce
data = lines(get_data(day=2,year=2021))

print(reduce(lambda a,b: a*b,
             map(sum, zip(*[(int(dist), 0) if inst == 'forward' else
                            (0, (-1 if inst == 'up' else 1) * int(dist))
                            for inst, dist in (r.split(" ") for r in data)]))))
