from aocd import get_data
from aocd.transforms import lines
from functools import reduce
data = lines(get_data(day=2,year=2021))

print(reduce(lambda a,b: (a or 1) * (b or 1),
             map(lambda t: t[0] * t[1],
                 zip([0,1,1],
                     reduce(lambda o, n: (
                               (o[0], o[1]+n[1], o[2]+(n[1] * o[0])) if n[0] == 'forward' else
                               (o[0] + n[1], o[1], o[2]) if n[0] == 'down' else
                               (o[0] - n[1], o[1], o[2])),
                            ((inst, int(dist))
                             for inst, dist in (r.split(" ") for r in data)),
                            (0,0,0))))))
