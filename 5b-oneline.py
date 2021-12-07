from aocd import get_data
from aocd.transforms import lines
from functools import reduce
from itertools import repeat
data = lines(get_data(year=2021,day=5))

print(reduce(
    lambda state, kv: (state + (1 if kv[1] > 1 else 0)),
    reduce(
        lambda state, line: (
        (x_range := (repeat(line[0][0]) if line[0][0] == line[1][0] else list(range(*(
            (line[0][0], line[1][0]+1, 1) if line[0][0] < line[1][0] else (line[0][0], line[1][0]-1,-1)
        ))))) and
        (y_range := (repeat(line[0][1]) if line[0][1] == line[1][1] else list(range(*(
            (line[0][1], line[1][1]+1, 1) if line[0][1] < line[1][1] else (line[0][1], line[1][1]-1,-1)
        ))))) and
        (reduce(
            lambda state, xy_pair: (
                (state.update({xy_pair: (state.get(xy_pair,0) + 1)}) or state)
            ),
            list(zip(x_range, y_range)),
            state
        ))),
    list(map(lambda line: list(map(lambda s: list(map(int, s.split(","))),
                                   line.split(" -> "))), data)),
    {}).items(),
    0
))
