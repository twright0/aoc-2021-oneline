from aocd import get_data
from aocd.transforms import lines
from functools import reduce
data = lines(get_data(day=3,year=2021))

print(reduce(
    lambda a,b: a*b,
    map(lambda s: int(''.join(s),2),
        list(reduce(lambda d,pos: (
            ( d[0] if len(d[0]) == 1 else
              [row for row in d[0] if row[pos] == '1']
              if sum((row[pos] == '1') for row in d[0]) >= len(d[0])/2 else
              [row for row in d[0] if row[pos] == '0']
             ),
            ( d[1] if len(d[1]) == 1 else
              [row for row in d[1] if row[pos] == '0']
              if sum((row[pos] == '1') for row in d[1]) >= len(d[1])/2 else
              [row for row in d[1] if row[pos] == '1']
             )
        ),
             range(len(data[0])),(data,data[:]))))))
