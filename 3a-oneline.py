from aocd import get_data
from aocd.transforms import lines
from functools import reduce
data = lines(get_data(day=3,year=2021))

print(reduce(lambda a,b: int(a,2)*int(''.join('0' if c == '1' else '1' for c in b),2),
             [''.join(('1' if v >= (len(data)/2) else '0') for v in (
                 list(map(lambda col: sum(c == '1' for c in col),
                          zip(*data)))))]*2))
